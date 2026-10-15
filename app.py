            selected_trainees = st.multiselect("TRN Personeli", trainee_names)
            selected_flights = st.multiselect("Uçuş", flight_names)
        with f3:
            default_start = min((r["operasyon_tarihi"] for r in records), default=date.today())
            start_date = st.date_input("Başlangıç Tarihi", value=default_start)
            end_date = st.date_input("Bitiş Tarihi", value=date.today())

        query = search.strip().casefold()
        filtered = []
        for record in records:
            joined = " ".join([record["mentor_ad_soyad"], record["trn_sicil"], record["trn_ad_soyad"], record["ucus_bilgisi"], record["gorev_alani"], record["degerlendirme_notu"]]).casefold()
            trainee_full = f"{record['trn_sicil']} - {record['trn_ad_soyad']}"
            if query and query not in joined:
                continue
            if selected_mentors and record["mentor_ad_soyad"] not in selected_mentors:
                continue
            if selected_trainees and trainee_full not in selected_trainees:
                continue
            if selected_flights and record["ucus_bilgisi"] not in selected_flights:
                continue
            if not start_date <= record["operasyon_tarihi"] <= end_date:
                continue
            filtered.append(record)

        st.caption(f"{len(filtered)} değerlendirme gösteriliyor")
        if filtered:
            filtered_df = evaluations_dataframe(filtered)
            summary = filtered_df.groupby(["trn_sicil", "trn_ad_soyad"], as_index=False).agg(degerlendirme_sayisi=("kayit_id", "count"), ortalama_puan=("mentor_puani", "mean")).sort_values(["degerlendirme_sayisi", "ortalama_puan"], ascending=[False, False])
            summary["ortalama_puan"] = summary["ortalama_puan"].round(2)
            st.markdown('<div class="section-title">TRN Performans Özeti</div>', unsafe_allow_html=True)
            summary_columns = st.columns(min(3, len(summary)))
            for position, (_, row) in enumerate(summary.iterrows()):
                with summary_columns[position % len(summary_columns)]:
                    st.markdown(
                        f'<div class="info-card"><div class="info-label">{safe_html(row["trn_sicil"])}</div>'
                        f'<div class="info-value">{safe_html(row["trn_ad_soyad"])}</div>'
                        f'<div class="subtle">{int(row["degerlendirme_sayisi"])} uçuş kaydı · Ortalama {row["ortalama_puan"]}/4</div></div>',
                        unsafe_allow_html=True,
                    )
            score_summary = filtered_df.groupby("mentor_ad_soyad", as_index=False).agg(kayit_sayisi=("kayit_id", "count"), ortalama_puan=("mentor_puani", "mean"))
            score_summary["ortalama_puan"] = score_summary["ortalama_puan"].round(2)
            st.markdown('<div class="section-title">Mentor Aktivite Özeti</div>', unsafe_allow_html=True)
            mentor_columns = st.columns(min(3, len(score_summary)))
            for position, (_, row) in enumerate(score_summary.iterrows()):
                with mentor_columns[position % len(mentor_columns)]:
                    st.markdown(
                        f'<div class="info-card"><div class="info-label">Mentor</div>'
                        f'<div class="info-value">{safe_html(row["mentor_ad_soyad"])}</div>'
                        f'<div class="subtle">{int(row["kayit_sayisi"])} değerlendirme · Ortalama {row["ortalama_puan"]}/4</div></div>',
                        unsafe_allow_html=True,
                    )
            st.markdown('<div class="section-title">Filtrelenmiş Değerlendirmeler</div>', unsafe_allow_html=True)
            render_evaluation_cards(filtered, show_mentor=True)
        else:
            st.info("Seçilen filtrelere uygun kayıt bulunamadı.")

    with readiness_tab:
        st.markdown('<div class="section-title">10 Uçuş Süreci ve Nihai Uygunluk Kontrolü</div>', unsafe_allow_html=True)
        st.caption("Bu ekran operasyonel bir öneri üretir. Yetkili kararı ve gerekli taşıyıcı onayı ayrıca tamamlanmalıdır.")
        for trainee in st.session_state.trainees:
            readiness = calculate_trainee_readiness(trainee["code"])
            recommendation = "Bağımsız kontuar için uygunluk önerilir" if readiness["ready"] else "Mentörlü TRN süreci devam etmeli"
            accent = "#16845B" if readiness["ready"] else "#E49B00"
            checks = [
                ("10 uçuş kaydı", readiness["ten_flights_complete"]),
                ("Son iki uçuşta 01–18 ≥ 3", readiness["basic_ready"]),
                ("19–26 ≥ 3 ve U/S kanıtlı", readiness["special_ready"]),
                ("Açık kritik bulgu yok", readiness["no_open_critical"]),
                ("Geri bildirimler tamam", readiness["feedback_complete"]),
            ]
            check_html = "".join(
                f'<span class="pill {"good" if passed else "warn"}">{"✓" if passed else "○"} {safe_html(label)}</span> '
                for label, passed in checks
            )
            st.markdown(
                f'<div class="evaluation-card" style="--card-accent:{accent}">'
                f'<div class="evaluation-head"><div><div class="evaluation-name">{safe_html(trainee_label(trainee))}</div>'
                f'<div class="evaluation-id">Mentor: {safe_html(st.session_state.users.get(trainee["mentor"], {}).get("full_name", trainee["mentor"]))}</div></div>'
                f'<div class="score-circle">{min(readiness["flight_count"], 10)}/10</div></div>'
                f'<div class="note-box"><b>{safe_html(recommendation)}</b><br>{check_html}</div></div>',
                unsafe_allow_html=True,
            )
            trainee_records = [r for r in records if r["trn_sicil"] == trainee["code"]]
            if trainee_records:
                with st.expander(f"{trainee['code']} uçuş kayıtlarını aç"):
                    render_evaluation_cards(trainee_records, show_mentor=True)

    with audit_tab:
        st.markdown('<div class="section-title">Kronolojik Denetim Kaydı</div>', unsafe_allow_html=True)
        if not records:
            st.info("Denetim kaydı bulunmuyor.")
        else:
            st.caption("Tüm kayıtlar en yeni değerlendirmeden başlayarak gösterilir.")
            render_evaluation_cards(records, show_mentor=True)

    with tools_tab:
        st.markdown('<div class="section-title">Raporlama ve Test Verisi Yönetimi</div>', unsafe_allow_html=True)
        st.markdown('<div class="hint">Dışa aktarılan UTF-8 CSV dosyası Excel ile doğrudan açılabilir. Sıfırlama işlemi mevcut oturumdaki kayıtları örnek veri setine döndürür.</div>', unsafe_allow_html=True)
        t1, t2 = st.columns(2)
        with t1:
            st.download_button("Tüm Değerlendirme Raporunu İndir", data=csv_bytes(records), file_name=f"istasyon_trn_tum_rapor_{date.today():%Y%m%d}.csv", mime="text/csv", use_container_width=True)
        with t2:
            if st.button("Verileri Sıfırla / Örnek Verileri Yükle", use_container_width=True):
                reset_demo_data()
                st.toast("Örnek veriler yeniden yüklendi.", icon="✅")
                st.rerun()

        st.markdown('<div class="section-title">Mentor Hesapları ve Atamalar</div>', unsafe_allow_html=True)
        accounts = []
        for key, user in st.session_state.users.items():
            assigned_names = [trainee_label(t) for t in st.session_state.trainees if t["mentor"] == key]
            accounts.append({"Kullanıcı Adı": key, "Mentor": user["full_name"], "Atanan TRN Sayısı": len(assigned_names), "Atanan Personel": ", ".join(assigned_names) or "Atama yok"})
        st.dataframe(pd.DataFrame(accounts), use_container_width=True, hide_index=True)


# =============================================================================
# ROL BAZLI UYGULAMA YÖNLENDİRMESİ
# =============================================================================
if not st.session_state.authenticated:
    authentication_page()
elif st.session_state.role == "mentor":
    mentor_panel()
elif st.session_state.role == "admin":
    admin_console()
else:
    logout()
    st.rerun()
