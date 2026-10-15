import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta


# =============================================================================
# SAYFA AYARLARI VE KURUMSAL TASARIM
# =============================================================================
st.set_page_config(
    page_title="İstasyon TRN Takip Portalı",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root {
        --navy:#05164D; --yellow:#FFAC00; --bg:#F4F6F9; --white:#FFFFFF;
        --green:#16845B; --red:#C93F49; --text:#18243D; --muted:#738096;
    }
    html, body, [class*="css"] { font-family:'Inter',sans-serif; }
    .stApp { background:var(--bg); color:var(--text); }
    .block-container { max-width:1450px; padding-top:1.35rem; padding-bottom:3rem; }
    #MainMenu, footer { visibility:hidden; }
    .hero { background:linear-gradient(125deg,#05164D 0%,#0A2B70 72%,#153A83 100%);
        border-radius:18px; padding:24px 28px; color:white; margin-bottom:18px;
        box-shadow:0 12px 30px rgba(5,22,77,.18); position:relative; overflow:hidden; }
    .hero:after { content:""; position:absolute; width:180px; height:180px;
        border:30px solid rgba(255,172,0,.14); border-radius:50%; right:-55px; top:-76px; }
    .hero-row { display:flex; gap:17px; align-items:center; position:relative; z-index:2; }
    .brand-badge { width:58px; height:58px; min-width:58px; border-radius:50%;
        display:flex; align-items:center; justify-content:center; background:var(--yellow);
        color:var(--navy); font-size:28px; box-shadow:0 5px 16px rgba(0,0,0,.18); }
    .hero h1 { margin:0; font-size:clamp(1.35rem,3vw,2.15rem); letter-spacing:-.03em; }
    .hero p { margin:6px 0 0; opacity:.82; font-size:.92rem; }
    .login-wrap { max-width:760px; margin:16px auto 0; }
    .login-shell { background:linear-gradient(145deg,#FFFFFF 0%,#F7F9FD 100%);
        border:1px solid #DFE6F0; border-radius:20px; padding:24px;
        box-shadow:0 18px 48px rgba(5,22,77,.11); margin-bottom:14px; }
    .login-intro { display:grid; grid-template-columns:1.35fr .65fr; gap:18px;
        align-items:center; margin-bottom:18px; }
    .login-title { color:var(--navy); font-size:1.35rem; font-weight:850; line-height:1.25; }
    .login-copy { color:#6C788D; font-size:.84rem; margin-top:7px; line-height:1.6; }
    .login-shield { width:74px; height:74px; margin-left:auto; border-radius:20px;
        display:flex; align-items:center; justify-content:center; font-size:34px;
        color:var(--navy); background:linear-gradient(145deg,#FFBE35,#FFAC00);
        box-shadow:0 9px 22px rgba(255,172,0,.25); }
    .feature-row { display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin:12px 0 18px; }
    .feature-chip { background:#F1F4FA; color:#43516B; border-radius:10px; padding:9px;
        font-size:.72rem; font-weight:700; text-align:center; border:1px solid #E5EAF2; }
    div[data-testid="stForm"] { background:white; border:1px solid #E4E9F0; border-radius:14px;
        padding:18px; box-shadow:0 5px 18px rgba(15,33,65,.06); }
    .eyebrow { color:#8C6500; font-size:.72rem; font-weight:800; letter-spacing:.08em;
        text-transform:uppercase; margin-bottom:5px; }
    .section-title { color:var(--navy); font-size:1.12rem; font-weight:800; margin:18px 0 10px; }
    .subtle { color:var(--muted); font-size:.8rem; }
    .metric-card { background:white; border-radius:14px; padding:17px 18px; min-height:120px;
        box-shadow:0 5px 18px rgba(15,33,65,.07); border-top:4px solid var(--accent); }
    .metric-label { color:#697386; font-size:.75rem; font-weight:700; text-transform:uppercase;
        letter-spacing:.05em; min-height:35px; }
    .metric-value { color:var(--navy); font-size:1.9rem; font-weight:800; margin-top:7px; }
    .metric-note { color:#8B95A7; font-size:.72rem; }
    .info-card { background:white; border:1px solid #E5EAF0; border-radius:13px;
        padding:15px 17px; box-shadow:0 3px 12px rgba(20,33,61,.05); height:100%; }
    .info-label { color:#8893A4; font-size:.69rem; text-transform:uppercase; font-weight:800; }
    .info-value { color:var(--navy); font-size:1rem; font-weight:750; margin-top:3px; }
    .demo-box { background:#FFF8E5; border:1px solid #F0D58C; border-radius:10px;
        padding:11px 13px; color:#68501B; font-size:.78rem; }
    .hint { background:#EDF3FF; border-left:4px solid #315AAB; border-radius:8px;
        padding:10px 13px; color:#2A3D65; font-size:.82rem; }
    .audit-note { background:#fff; border:1px solid #E5E9EF; border-radius:11px;
        padding:12px 14px; margin:7px 0; }
    .evaluation-card { background:#FFFFFF; border:1px solid #E2E7EF; border-radius:16px;
        padding:18px; margin:8px 0 14px; box-shadow:0 7px 22px rgba(12,31,71,.07);
        position:relative; overflow:hidden; min-height:305px; }
    .evaluation-card:before { content:""; position:absolute; left:0; top:0; bottom:0;
        width:5px; background:var(--card-accent,#315AAB); }
    .evaluation-head { display:flex; justify-content:space-between; align-items:flex-start;
        gap:10px; padding-left:3px; }
    .evaluation-name { color:var(--navy); font-size:1.02rem; font-weight:850; }
    .evaluation-id { color:#8993A3; font-size:.69rem; margin-top:3px; }
    .score-circle { width:46px; height:46px; min-width:46px; border-radius:50%;
        display:flex; align-items:center; justify-content:center; color:white;
        background:var(--card-accent,#315AAB); font-weight:850; font-size:1rem; }
    .flight-band { display:flex; justify-content:space-between; align-items:center; gap:8px;
        background:#F3F6FB; border-radius:10px; padding:10px 11px; margin:14px 0 12px;
        color:#243651; font-weight:750; font-size:.77rem; }
    .evaluation-grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px; }
    .evaluation-label { color:#929CAB; font-size:.63rem; font-weight:800;
        text-transform:uppercase; letter-spacing:.04em; }
    .evaluation-value { color:#334058; font-size:.76rem; font-weight:650; margin-top:2px; }
    .note-box { background:#F8FAFD; border-radius:9px; padding:10px 11px; margin-top:8px;
        color:#46536A; font-size:.75rem; line-height:1.45; border:1px solid #EDF0F5; }
    .pill { display:inline-block; border-radius:999px; padding:5px 9px; font-size:.65rem;
        font-weight:800; background:#E7EDFF; color:#244698; }
    .pill.good { background:#E2F5EC; color:#08734A; }
    .pill.warn { background:#FFF0CF; color:#8A5700; }
    .pill.bad { background:#FBE4E6; color:#A52D38; }
    .stButton > button, .stDownloadButton > button {
        border-radius:10px !important; font-weight:750 !important; min-height:43px; width:100%;
        background:#05164D !important; color:#FFFFFF !important; border:1px solid #05164D !important;
        box-shadow:0 5px 13px rgba(5,22,77,.16) !important; transition:.18s ease !important; }
    .stButton > button:hover, .stDownloadButton > button:hover {
        background:#FFAC00 !important; color:#05164D !important; border-color:#FFAC00 !important;
        transform:translateY(-1px); box-shadow:0 7px 16px rgba(255,172,0,.23) !important; }
    .stButton > button:disabled { background:#A8B1C1 !important; border-color:#A8B1C1 !important;
        color:#F7F8FA !important; opacity:1 !important; }
    .stButton > button p, .stDownloadButton > button p { color:inherit !important; }
    div[data-baseweb="tab-list"] { gap:7px; }
    button[data-baseweb="tab"] { background:white; border-radius:10px; padding:9px 15px; }
    button[data-baseweb="tab"][aria-selected="true"] { background:#05164D !important;
        color:#FFFFFF !important; }
    [data-testid="stDataFrame"] { background:white; border-radius:12px; overflow:auto; }
    @media (max-width:768px) {
        .block-container { padding:11px 11px 34px; }
        .hero { padding:19px 16px; border-radius:14px; }
        .brand-badge { width:47px; height:47px; min-width:47px; font-size:22px; }
        .hero p { font-size:.78rem; }
        .metric-card { min-height:103px; padding:13px; margin-bottom:4px; }
        .metric-value { font-size:1.55rem; }
        div[data-testid="stHorizontalBlock"] { gap:.55rem; }
        .stButton > button, .stDownloadButton > button { width:100%; }
        .login-shell { padding:16px; border-radius:15px; }
        .login-intro { grid-template-columns:1fr; }
        .login-shield { margin:0; width:58px; height:58px; font-size:27px; }
        .feature-row { grid-template-columns:1fr; }
        .evaluation-card { min-height:unset; padding:15px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =============================================================================
# SABİTLER VE ÖRNEK VERİ ÜRETİCİLERİ
# =============================================================================
ADMIN_PASSWORD = "chef2026"

FLIGHTS = [
    "FL1299 - A320 / MUC", "FL1301 - A321 / FRA", "FL1305 - A320 / FRA",
    "FL1313 - A321 / MUC", "FL1407 - A320 / STR", "FL1411 - A321 / DUS",
]

DUTIES = [
    "Check-in İşlemleri", "Boarding Operasyonu", "Doküman Kontrolü",
    "Bagaj / Gate Sorun Çözümü", "Transfer Yolcu İşlemleri",
    "Özel Hizmet Gerektiren Yolcu",
]

SHIFTS = ["03:40–11:40", "09:00–17:00", "14:30–22:30", "Diğer"]
COMPETENCIES = ["Başarılı", "Geliştirilmeli", "Kritik Hata"]
PROCESS_STATUSES = ["Eğitimde", "İzlemede", "Değerlendirme Aşaması", "Release Uygun", "Release Verildi"]

# Word formundaki 1–4/G ölçeği ve kanıt türleri
SCORE_OPTIONS = ["G", "1", "2", "3", "4"]
EVIDENCE_OPTIONS = ["-", "U", "S", "T"]
SUPPORT_LEVELS = ["Yoğun destek gerekli", "Kısmi destek gerekli", "Bağımsız uygulama gözlendi"]
FINDING_STATUSES = ["Yok", "Kapandı", "Açık"]
MENTOR_RECOMMENDATIONS = [
    "Değerlendirme Bekliyor",
    "Tek başına kontuar görevi için uygun",
    "Ek mentörlü TRN gerekli",
]
AUTHORIZED_DECISIONS = [
    "Karar Bekliyor",
    "Tek başına planlama onaylandı",
    "Ek TRN",
    "Taşıyıcı onayı bekleniyor",
]
CRITICAL_ITEMS = {"06", "07", "08", "10", "11", "13", "15", "17", "18"}

BASIC_ITEMS = {
    "01": "Üniforma, görünüm, görev saati ve çalışma planına uyum",
    "02": "Kontuar, tartı/bant, yazıcı, malzeme ve etiket hazırlığı",
    "03": "Brifing, uçuş mesajları, bağlantı ve özel yolcu bilgisi kontrolü",
    "04": "Karşılama, göz teması, selamlama ve yolcunun ismini kullanma",
    "05": "Anlaşılır İngilizce, olumlu dil, empati ve açık yönlendirme",
    "06": "Yolcu, kimlik, bilet ve rezervasyonu eşleştirerek doğru kabul yapma",
    "07": "Seyahat belgesi, vize ve transit şartlarını yetkili kaynaktan doğrulama",
    "08": "DCS üzerinde uçuş, tarih, güzergâh ve kabul uygunluğunu doğrulama",
    "09": "Yolcu bilgileri, rezervasyon bağlantıları ve SSR kayıtlarını yorumlama",
    "10": "Koltuk tercihi, ASR ve kısıtlı koltuk uygunluğunu doğru uygulama",
    "11": "DGR ve güvenlik soruları ile şüpheli durumda doğru eskalasyon",
    "12": "Bagaj hakkı, parça, ağırlık, ölçü ve uçuş uygunluğunu kontrol etme",
    "13": "Bagajı doğru yolcu ve varışa kaydetme, etiket ve kupon kontrolü",
    "14": "Kabin bagajını güncel taşıyıcı kurallarına göre kontrol etme",
    "15": "Biniş kartı bilgilerini doğrulayıp doğru yolcuya teslim etme",
    "16": "Gate, boarding saati ve bağlantı bilgileriyle doğru yönlendirme",
    "17": "Yolcu verisi, ekran, çıktı ve evrak imhasında veri güvenliği",
    "18": "Yetkili kaynak kullanma, yetki sınırına uyma ve hatayı bildirme",
}

SPECIAL_ITEMS = {
    "19": "Fazla bagaj, ödenmiş hizmet belgesi ve yetki içi tahsilat",
    "20": "Bağlantılı yolcu ve bagaj kabulünü taşıyıcı kurallarına göre yapma",
    "21": "Spor veya özel bagaj, gerekli SSR ve sistem girişleri",
    "22": "PRM/WCH ihtiyacı ve hareket yardımcısının doğru kabulü",
    "23": "UM yolcu yaşı, onayı, ödeme ve teslim belgeleri",
    "24": "PETC/AVIH ve hizmet hayvanı kabul şartları, onay ve belgeler",
    "25": "Staff/crew bileti, seyahat hakkı, öncelik ve sistem kabulü",
    "26": "Kabul iptali veya uçuş aksaklığında doğru işlem ve eskalasyon",
}


def seed_users():
    """Prototip için örnek mentor hesaplarını döndürür."""
    return {
        "selin.kaya": {"password": "mentor123", "full_name": "Selin Kaya"},
        "murat.aksoy": {"password": "mentor123", "full_name": "Murat Aksoy"},
        "burak.sahin": {"password": "mentor123", "full_name": "Burak Şahin"},
    }


def seed_trainees():
    """Mentor atamalarını da içeren örnek TRN personel havuzu."""
    return [
        {"code": "TR1042", "name": "Ahmet Yılmaz", "mentor": "selin.kaya", "status": "Eğitimde", "station": "IST", "class_end": date.today() - timedelta(days=18), "trn_start": date.today() - timedelta(days=15), "trn_end": None, "prerequisites": "Sınıf eğitimi ve sistem yetkileri kontrol edildi"},
        {"code": "TR1087", "name": "Elif Demir", "mentor": "murat.aksoy", "status": "Değerlendirme Aşaması", "station": "IST", "class_end": date.today() - timedelta(days=40), "trn_start": date.today() - timedelta(days=36), "trn_end": None, "prerequisites": "Ön koşullar tamamlandı"},
        {"code": "TR1115", "name": "Can Eren", "mentor": "selin.kaya", "status": "İzlemede", "station": "IST", "class_end": date.today() - timedelta(days=25), "trn_start": date.today() - timedelta(days=22), "trn_end": None, "prerequisites": "Doküman kontrol tekrar eğitimi planlandı"},
        {"code": "TR1168", "name": "Zeynep Arslan", "mentor": "burak.sahin", "status": "Release Uygun", "station": "IST", "class_end": date.today() - timedelta(days=65), "trn_start": date.today() - timedelta(days=60), "trn_end": date.today(), "prerequisites": "Tüm eğitim ve yetki ön koşulları tamamlandı"},
        {"code": "TR1203", "name": "Mert Çelik", "mentor": "murat.aksoy", "status": "Eğitimde", "station": "IST", "class_end": date.today() - timedelta(days=12), "trn_start": date.today() - timedelta(days=9), "trn_end": None, "prerequisites": "Sistem yetkisi aktif"},
        {"code": "TR1249", "name": "Derya Koç", "mentor": "burak.sahin", "status": "İzlemede", "station": "IST", "class_end": date.today() - timedelta(days=30), "trn_start": date.today() - timedelta(days=27), "trn_end": None, "prerequisites": "Ön koşullar tamamlandı"},
    ]


def seed_evaluations():
    """IST çıkışlı maskeli uçuşlarla gerçekçi örnek değerlendirmeler."""
    today = date.today()
    samples = [
        ("EV-0001", 8, "selin.kaya", "Selin Kaya", "TR1042", "Ahmet Yılmaz", "09:00–17:00", FLIGHTS[1], DUTIES[0], 4, "Başarılı", "DCS adımlarını doğru uyguladı; işlem hızı gelişiyor.", "Yoğun uçuşta süre takibi yapılacak.", "Eğitimde"),
        ("EV-0002", 7, "murat.aksoy", "Murat Aksoy", "TR1087", "Elif Demir", "03:40–11:40", FLIGHTS[0], DUTIES[2], 5, "Başarılı", "Seyahat dokümanlarını eksiksiz kontrol etti.", "Final gözlem planlanabilir.", "Release Uygun"),
        ("EV-0003", 5, "selin.kaya", "Selin Kaya", "TR1115", "Can Eren", "14:30–22:30", FLIGHTS[3], DUTIES[1], 2, "Geliştirilmeli", "Boarding anons sıralamasında desteğe ihtiyaç duydu.", "Bir sonraki uçuşta anons akışı tekrar edilmeli.", "İzlemede"),
        ("EV-0004", 4, "burak.sahin", "Burak Şahin", "TR1168", "Zeynep Arslan", "09:00–17:00", FLIGHTS[4], DUTIES[3], 5, "Başarılı", "Irregularity senaryosunu bağımsız yönetti.", "Release değerlendirmesi olumlu.", "Release Uygun"),
        ("EV-0005", 2, "murat.aksoy", "Murat Aksoy", "TR1203", "Mert Çelik", "09:00–17:00", FLIGHTS[2], DUTIES[2], 1, "Kritik Hata", "Vize kontrol adımında doğrulama desteği gerekti.", "Doküman eğitimi yenilenmeli ve çift kontrol uygulanmalı.", "Eğitimde"),
        ("EV-0006", 1, "burak.sahin", "Burak Şahin", "TR1249", "Derya Koç", "14:30–22:30", FLIGHTS[5], DUTIES[1], 4, "Başarılı", "Boarding kapanış ve mutabakat adımlarını doğru tamamladı.", "Bir ek yoğun uçuş gözlemi önerilir.", "İzlemede"),
    ]
    output = []
    for flight_no, sample in enumerate(samples, start=1):
        record_id, days_ago, username, mentor, code, trainee, shift, flight, duty, score, competency, note, action, status = sample
        operation_day = today - timedelta(days=days_ago)
        base_score = str(max(1, min(4, score)))
        basic_scores = {item_no: base_score for item_no in BASIC_ITEMS}
        if competency == "Kritik Hata":
            basic_scores["07"] = "1"
        elif competency == "Geliştirilmeli":
            basic_scores["05"] = "2"
            basic_scores["16"] = "2"
        special_scores = {item_no: "G" for item_no in SPECIAL_ITEMS}
        special_evidence = {item_no: "-" for item_no in SPECIAL_ITEMS}
        if flight_no in {2, 4, 6}:
            observed_item = {2: "22", 4: "26", 6: "19"}[flight_no]
            special_scores[observed_item] = base_score
            special_evidence[observed_item] = "U"
        output.append({
            "kayit_id": record_id,
            "zaman_damgasi": f"{operation_day:%Y-%m-%d} 12:00:00",
            "mentor_kullanici": username,
            "mentor_ad_soyad": mentor,
            "trn_sicil": code,
            "trn_ad_soyad": trainee,
            "operasyon_tarihi": operation_day,
            "vardiya": shift,
            "ucus_bilgisi": flight,
            "gorev_alani": duty,
            # Özet puan artık Word formundaki 01–18 maddesinin 1–4 ortalamasıdır.
            "mentor_puani": round(
                sum(int(value) for value in basic_scores.values() if value.isdigit())
                / len([value for value in basic_scores.values() if value.isdigit()]),
                2,
            ),
            "yetkinlik_seviyesi": competency,
            "degerlendirme_notu": note,
            "aksiyon_maddeleri": action,
            "surec_durumu": status,
            "son_guncelleme": f"{operation_day:%Y-%m-%d} 12:00:00",
            "ucus_no": flight_no,
            "parkur": flight.split("/")[-1].strip(),
            "ucak_tipi": flight.split("-")[1].split("/")[0].strip(),
            "kontuar_no": str(20 + flight_no),
            "islem_yolcu_sayisi": 8 + flight_no * 2,
            "temel_puanlar": basic_scores,
            "ozel_puanlar": special_scores,
            "ozel_kanitlar": special_evidence,
            "gozlem_egitim_kaydi": note,
            "kritik_mudahale": competency == "Kritik Hata",
            "kritik_madde_no": "07" if competency == "Kritik Hata" else "",
            "onceki_bulgu_durumu": "Açık" if competency == "Kritik Hata" else "Yok",
            "kapanis_kaniti": "" if competency == "Kritik Hata" else "Ek kapanış kanıtı gerekmiyor.",
            "guclu_yon": note,
            "sonraki_hedef": action,
            "sorumlu_kisi": mentor,
            "hedef_ucus_tarih": operation_day + timedelta(days=3),
            "destek_seviyesi": "Yoğun destek gerekli" if competency == "Kritik Hata" else ("Kısmi destek gerekli" if competency == "Geliştirilmeli" else "Bağımsız uygulama gözlendi"),
            "geri_bildirim_onayi": True,
            "mentor_dijital_onay": True,
            "mentor_onay_zamani": f"{operation_day:%Y-%m-%d} 12:00:00",
            "personel_onay_zamani": f"{operation_day:%Y-%m-%d} 12:05:00",
        })
    return output


# =============================================================================
# SESSION STATE VE ORTAK YARDIMCI FONKSİYONLAR
# =============================================================================
def initialize_state():
    defaults = {
        "users": seed_users(), "trainees": seed_trainees(), "evaluations": seed_evaluations(),
        "final_decisions": {}, "authenticated": False, "role": None,
        "username": None, "full_name": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # Önceki prototip oturumlarındaki kayıtları yeni detaylı modele taşır.
    for index, record in enumerate(st.session_state.evaluations, start=1):
        fallback_score = str(max(1, min(4, int(record.get("mentor_puani", 3)))))
        record.setdefault("ucus_no", index)
        record.setdefault("parkur", record.get("ucus_bilgisi", " / ").split("/")[-1].strip())
        record.setdefault("ucak_tipi", "")
        record.setdefault("kontuar_no", "")
        record.setdefault("islem_yolcu_sayisi", 0)
        record.setdefault("temel_puanlar", {item_no: fallback_score for item_no in BASIC_ITEMS})
        record.setdefault("ozel_puanlar", {item_no: "G" for item_no in SPECIAL_ITEMS})
        record.setdefault("ozel_kanitlar", {item_no: "-" for item_no in SPECIAL_ITEMS})
        record.setdefault("gozlem_egitim_kaydi", record.get("degerlendirme_notu", ""))
        record.setdefault("kritik_mudahale", record.get("yetkinlik_seviyesi") == "Kritik Hata")
        record.setdefault("kritik_madde_no", "")
        record.setdefault("onceki_bulgu_durumu", "Yok")
        record.setdefault("kapanis_kaniti", "")
        record.setdefault("guclu_yon", record.get("degerlendirme_notu", ""))
        record.setdefault("sonraki_hedef", record.get("aksiyon_maddeleri", ""))
        record.setdefault("sorumlu_kisi", record.get("mentor_ad_soyad", ""))
        record.setdefault("hedef_ucus_tarih", record.get("operasyon_tarihi", date.today()))
        record.setdefault("destek_seviyesi", "Kısmi destek gerekli")
        record.setdefault("geri_bildirim_onayi", False)
        record.setdefault("mentor_dijital_onay", False)
        record.setdefault("mentor_onay_zamani", "")
        record.setdefault("personel_onay_zamani", "")


def logout():
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = None
    st.session_state.full_name = None


def reset_demo_data():
    st.session_state.users = seed_users()
    st.session_state.trainees = seed_trainees()
    st.session_state.evaluations = seed_evaluations()
    st.session_state.final_decisions = {}


def make_record_id():
    return "EV-" + datetime.now().strftime("%Y%m%d%H%M%S%f")


def trainee_label(item):
    return f"{item['code']} - {item['name']}"


def evaluations_dataframe(records):
    base_columns = [
        "kayit_id", "zaman_damgasi", "mentor_ad_soyad", "trn_sicil", "trn_ad_soyad",
        "ucus_no", "operasyon_tarihi", "vardiya", "ucus_bilgisi", "parkur", "ucak_tipi",
        "kontuar_no", "islem_yolcu_sayisi", "gorev_alani", "mentor_puani",
        "yetkinlik_seviyesi", "degerlendirme_notu", "aksiyon_maddeleri", "surec_durumu",
        "gozlem_egitim_kaydi", "kritik_mudahale", "kritik_madde_no", "onceki_bulgu_durumu",
        "kapanis_kaniti", "guclu_yon", "sonraki_hedef", "sorumlu_kisi", "hedef_ucus_tarih",
        "destek_seviyesi", "geri_bildirim_onayi", "son_guncelleme",
        "mentor_dijital_onay", "mentor_onay_zamani", "personel_onay_zamani",
    ]
    metric_columns = ["temel_toplam", "temel_puanlanan", "temel_ortalama", "g_maddeleri", "dusuk_maddeler", "kritik_dusuk_maddeler"]
    score_columns = [f"temel_{item_no}" for item_no in BASIC_ITEMS]
    special_columns = [value for item_no in SPECIAL_ITEMS for value in (f"ozel_{item_no}", f"kanit_{item_no}")]
    columns = base_columns + metric_columns + score_columns + special_columns
    flattened = []
    for record in records:
        row = {column: record.get(column, "") for column in base_columns}
        metrics = calculate_flight_metrics(record)
        row.update({
            "temel_toplam": metrics["total"], "temel_puanlanan": metrics["rated"],
            "temel_ortalama": metrics["average"], "g_maddeleri": ", ".join(metrics["g_items"]),
            "dusuk_maddeler": ", ".join(metrics["low_items"]),
            "kritik_dusuk_maddeler": ", ".join(metrics["critical_low"]),
        })
        for item_no in BASIC_ITEMS:
            row[f"temel_{item_no}"] = record.get("temel_puanlar", {}).get(item_no, "G")
        for item_no in SPECIAL_ITEMS:
            row[f"ozel_{item_no}"] = record.get("ozel_puanlar", {}).get(item_no, "G")
            row[f"kanit_{item_no}"] = record.get("ozel_kanitlar", {}).get(item_no, "-")
        flattened.append(row)
    df = pd.DataFrame(flattened)
    if df.empty:
        return pd.DataFrame(columns=columns)
    for col in columns:
        if col not in df.columns:
            df[col] = ""
    return df[columns].sort_values(["operasyon_tarihi", "zaman_damgasi"], ascending=False)


def csv_bytes(records):
    return evaluations_dataframe(records).to_csv(index=False, sep=";", encoding="utf-8-sig").encode("utf-8-sig")


def final_decisions_dataframe():
    """Belgedeki gelişim özeti ve nihai karar alanlarını tek raporda birleştirir."""
    rows = []
    for trainee in st.session_state.trainees:
        readiness = calculate_trainee_readiness(trainee["code"])
        decision = st.session_state.final_decisions.get(trainee["code"], {})
        rows.append({
            "trn_sicil": trainee["code"],
            "trn_ad_soyad": trainee["name"],
            "istasyon": trainee.get("station", ""),
            "sinif_egitimi_bitis": trainee.get("class_end", ""),
            "trn_baslangic": trainee.get("trn_start", ""),
            "trn_bitis": trainee.get("trn_end", ""),
            "on_kosul_kaydi": trainee.get("prerequisites", ""),
            "tamamlanan_ucus": readiness["flight_count"],
            "son_iki_ucus": ", ".join(map(str, readiness["last_two_flights"])),
            "son_iki_ucus_uygun": readiness["basic_ready"],
            "ozel_durum_uygun": readiness["special_ready"],
            "acik_kritik_bulgu_yok": readiness["no_open_critical"],
            "geri_bildirim_imzalari_tamam": readiness["feedback_complete"],
            "egitim_sure_yetki_tamam": decision.get("egitim_sure_yetki_tamam", False),
            "mentor_onerisi": decision.get("mentor_onerisi", "Değerlendirme Bekliyor"),
            "yetkili_karar": decision.get("yetkili_karar", "Karar Bekliyor"),
            "gerekce": decision.get("gerekce", ""),
            "gorev_kapsami": decision.get("gorev_kapsami", ""),
            "planlama_baslangic": decision.get("planlama_baslangic", ""),
            "tasiyici_onay_no": decision.get("tasiyici_onay_no", ""),
            "mentor_imza": decision.get("mentor_imza", ""),
            "yonetici_imza": decision.get("yonetici_imza", ""),
            "tasiyici_yetkilisi": decision.get("tasiyici_yetkilisi", ""),
            "planlamaya_bildiren": decision.get("planlamaya_bildiren", ""),
            "yetkili_dijital_onay": decision.get("yetkili_dijital_onay", False),
            "yetkili_onay_zamani": decision.get("yetkili_onay_zamani", ""),
        })
    return pd.DataFrame(rows)


def final_csv_bytes():
    return final_decisions_dataframe().to_csv(index=False, sep=";", encoding="utf-8-sig").encode("utf-8-sig")


def render_header(subtitle):
    st.markdown(
        f"""<div class="hero"><div class="hero-row"><div class="brand-badge">✈</div>
        <div><h1>İstasyon TRN Takip ve Değerlendirme Portalı</h1><p>{subtitle}</p></div>
        </div></div>""",
        unsafe_allow_html=True,
    )


def render_metric(label, value, note, color):
    st.markdown(
        f'<div class="metric-card" style="--accent:{color}"><div class="metric-label">{label}</div>'
        f'<div class="metric-value">{value}</div><div class="metric-note">{note}</div></div>',
        unsafe_allow_html=True,
    )


def safe_html(value):
    """Kullanıcı metinlerini HTML kartlarında güvenli biçimde gösterir."""
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
        .replace("\n", "<br>")
    )


def calculate_flight_metrics(record):
    """Belgedeki kurala göre temel puan, ortalama, G ve kritik bulguları hesaplar."""
    scores = record.get("temel_puanlar", {})
    numeric = [int(value) for value in scores.values() if str(value).isdigit()]
    total = sum(numeric)
    average = round(total / len(numeric), 2) if numeric else 0.0
    g_items = [item_no for item_no, value in scores.items() if value == "G"]
    low_items = [item_no for item_no, value in scores.items() if str(value) in {"1", "2"}]
    critical_low = [item_no for item_no in low_items if item_no in CRITICAL_ITEMS]
    return {
        "total": total,
        "rated": len(numeric),
        "average": average,
        "g_items": g_items,
        "low_items": low_items,
        "critical_low": critical_low,
    }


def calculate_trainee_readiness(trainee_code):
    """Son iki uçuş ve özel durum kanıtlarına göre öneri niteliğinde uygunluk üretir."""
    records = [
        record for record in st.session_state.evaluations
        if record["trn_sicil"] == trainee_code
    ]
    records = sorted(records, key=lambda item: (item.get("ucus_no", 0), item["zaman_damgasi"]))
    # Aynı uçuş numarası yanlışlıkla iki kez girilse bile süreç sayısını şişirmez.
    unique_flights = {}
    for record in records:
        unique_flights[int(record.get("ucus_no", 0))] = record
    completed_records = [unique_flights[number] for number in sorted(unique_flights)]
    standard_records = [record for record in completed_records if 1 <= int(record.get("ucus_no", 0)) <= 10]
    last_two = standard_records[-2:]
    ten_flights_complete = len(standard_records) >= 10
    basic_ready = len(last_two) == 2 and all(
        all(str(record.get("temel_puanlar", {}).get(item_no, "G")).isdigit()
            and int(record["temel_puanlar"][item_no]) >= 3 for item_no in BASIC_ITEMS)
        for record in last_two
    )
    special_latest = {}
    for record in completed_records:
        for item_no in SPECIAL_ITEMS:
            score = record.get("ozel_puanlar", {}).get(item_no, "G")
            evidence = record.get("ozel_kanitlar", {}).get(item_no, "-")
            if str(score).isdigit():
                special_latest[item_no] = (int(score), evidence)
    special_ready = all(
        item_no in special_latest
        and special_latest[item_no][0] >= 3
        and special_latest[item_no][1] in {"U", "S"}
        for item_no in SPECIAL_ITEMS
    )
    no_open_critical = not any(
        record.get("kritik_mudahale") and record.get("onceki_bulgu_durumu") == "Açık"
        for record in completed_records
    )
    feedback_complete = bool(standard_records) and all(
        record.get("geri_bildirim_onayi") and record.get("mentor_dijital_onay")
        for record in standard_records
    )
    final_decision = st.session_state.get("final_decisions", {}).get(trainee_code, {})
    external_conditions_ready = bool(final_decision.get("egitim_sure_yetki_tamam"))
    technical_ready = ten_flights_complete and basic_ready and special_ready and no_open_critical and feedback_complete
    ready = technical_ready and external_conditions_ready
    return {
        "flight_count": len(standard_records),
        "ten_flights_complete": ten_flights_complete,
        "basic_ready": basic_ready,
        "special_ready": special_ready,
        "no_open_critical": no_open_critical,
        "feedback_complete": feedback_complete,
        "external_conditions_ready": external_conditions_ready,
        "technical_ready": technical_ready,
        "last_two_flights": [record.get("ucus_no") for record in last_two],
        "authorized_decision": final_decision.get("yetkili_karar", "Karar Bekliyor"),
        "ready": ready,
    }


def render_evaluation_card(record, show_mentor=True):
    """Tek bir TRN değerlendirmesini modern ve responsive kart olarak çizer."""
    competency = record["yetkinlik_seviyesi"]
    if competency == "Başarılı":
        accent, pill_class = "#16845B", "good"
    elif competency == "Kritik Hata":
        accent, pill_class = "#C93F49", "bad"
    else:
        accent, pill_class = "#E49B00", "warn"

    operation_date = record["operasyon_tarihi"]
    if hasattr(operation_date, "strftime"):
        operation_date = operation_date.strftime("%d.%m.%Y")

    mentor_block = ""
    if show_mentor:
        mentor_block = (
            '<div><div class="evaluation-label">Mentor</div>'
            f'<div class="evaluation-value">{safe_html(record["mentor_ad_soyad"])}</div></div>'
        )

    action_text = record.get("aksiyon_maddeleri") or "Ek aksiyon girilmedi."
    metrics = calculate_flight_metrics(record)
    # HTML satırlarında baştaki dört boşluk Markdown tarafından kod bloğu
    # olarak yorumlanabildiği için kart tek ve girintisiz bir akışta üretilir.
    card_html = (
        f'<div class="evaluation-card" style="--card-accent:{accent}">'
        '<div class="evaluation-head">'
        '<div>'
        f'<div class="evaluation-name">Uçuş {record.get("ucus_no", "-")} · {safe_html(record["trn_sicil"])} · {safe_html(record["trn_ad_soyad"])}</div>'
        f'<div class="evaluation-id">{safe_html(record["kayit_id"])} · {safe_html(record["zaman_damgasi"])}</div>'
        '</div>'
        f'<div class="score-circle">{float(record["mentor_puani"]):.1f}/4</div>'
        '</div>'
        '<div class="flight-band">'
        f'<span>✈ {safe_html(record["ucus_bilgisi"])}</span>'
        f'<span class="pill {pill_class}">{safe_html(competency)}</span>'
        '</div>'
        '<div class="evaluation-grid">'
        '<div><div class="evaluation-label">Operasyon Tarihi</div>'
        f'<div class="evaluation-value">{operation_date}</div></div>'
        '<div><div class="evaluation-label">Vardiya</div>'
        f'<div class="evaluation-value">{safe_html(record["vardiya"])}</div></div>'
        '<div><div class="evaluation-label">Görev / Eğitim</div>'
        f'<div class="evaluation-value">{safe_html(record["gorev_alani"])}</div></div>'
        '<div><div class="evaluation-label">Süreç Durumu</div>'
        f'<div class="evaluation-value">{safe_html(record["surec_durumu"])}</div></div>'
        '<div><div class="evaluation-label">Temel Ortalama</div>'
        f'<div class="evaluation-value">{metrics["average"]} / 4 · {metrics["rated"]}/18 madde</div></div>'
        '<div><div class="evaluation-label">G / Düşük / Kritik</div>'
        f'<div class="evaluation-value">{len(metrics["g_items"])} / {len(metrics["low_items"])} / {len(metrics["critical_low"])}</div></div>'
        '<div><div class="evaluation-label">Kontuar / İşlem Yolcu</div>'
        f'<div class="evaluation-value">{safe_html(record.get("kontuar_no", "-"))} / {record.get("islem_yolcu_sayisi", 0)}</div></div>'
        '<div><div class="evaluation-label">Destek Seviyesi</div>'
        f'<div class="evaluation-value">{safe_html(record.get("destek_seviyesi", "-"))}</div></div>'
        f'{mentor_block}'
        '</div>'
        '<div class="note-box"><b>Mentor değerlendirmesi</b><br>'
        f'{safe_html(record["degerlendirme_notu"])}</div>'
        '<div class="note-box"><b>Aksiyon</b><br>'
        f'{safe_html(action_text)}</div>'
        '</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)


def render_evaluation_cards(records, show_mentor=True):
    """Değerlendirmeleri masaüstünde iki sütun, mobilde tek sütun gösterir."""
    if not records:
        st.info("Görüntülenecek değerlendirme bulunmuyor.")
        return
    ordered = sorted(records, key=lambda item: item["zaman_damgasi"], reverse=True)
    for index in range(0, len(ordered), 2):
        columns = st.columns(2)
        for offset, column in enumerate(columns):
            record_index = index + offset
            if record_index < len(ordered):
                with column:
                    render_evaluation_card(ordered[record_index], show_mentor=show_mentor)
                    render_competency_details(ordered[record_index])


def render_competency_details(record):
    """Puanları tablo yerine açılır, okunaklı madde kartlarıyla gösterir."""
    with st.expander(f"Uçuş {record.get('ucus_no', '—')} · Yetkinlik ve geri bildirim ayrıntıları"):
        st.markdown("**01–18 Temel Kontuar Yetkinlikleri**")
        blocks = []
        for item_no, description in BASIC_ITEMS.items():
            value = record.get("temel_puanlar", {}).get(item_no, "G")
            critical = " · Kritik" if item_no in CRITICAL_ITEMS else ""
            blocks.append(
                f'<div class="note-box"><b>{item_no}{critical} · Puan {safe_html(value)}</b><br>{safe_html(description)}</div>'
            )
        st.markdown("".join(blocks), unsafe_allow_html=True)
        st.markdown("**19–26 Özel Durumlar**")
        blocks = []
        for item_no, description in SPECIAL_ITEMS.items():
            value = record.get("ozel_puanlar", {}).get(item_no, "G")
            evidence = record.get("ozel_kanitlar", {}).get(item_no, "-")
            blocks.append(
                f'<div class="note-box"><b>{item_no} · Puan {safe_html(value)} · Kanıt {safe_html(evidence)}</b><br>{safe_html(description)}</div>'
            )
        st.markdown("".join(blocks), unsafe_allow_html=True)
        st.markdown(
            f'<div class="note-box"><b>Somut gözlem / eğitim kaydı</b><br>{safe_html(record.get("gozlem_egitim_kaydi") or "Kayıt yok")}</div>'
            f'<div class="note-box"><b>Güçlü yön</b><br>{safe_html(record.get("guclu_yon") or "Kayıt yok")}</div>'
            f'<div class="note-box"><b>Sonraki hedef</b><br>{safe_html(record.get("sonraki_hedef") or "Kayıt yok")}</div>'
            f'<div class="note-box"><b>Dijital teyitler</b><br>'
            f'Mentör: {"Tamamlandı" if record.get("mentor_dijital_onay") else "Eksik"} '
            f'({safe_html(record.get("mentor_onay_zamani") or "—")}) · '
            f'Personel geri bildirimi: {"Tamamlandı" if record.get("geri_bildirim_onayi") else "Eksik"} '
            f'({safe_html(record.get("personel_onay_zamani") or "—")})</div>',
            unsafe_allow_html=True,
        )


initialize_state()


# =============================================================================
# GİRİŞ VE MENTOR KAYIT EKRANI
# =============================================================================
def authentication_page():
    render_header("Yolcu Hizmetleri On-the-Job Training süreçleri için güvenli operasyon portalı")
    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="login-shell">
          <div class="login-intro">
            <div>
              <div class="eyebrow">Güvenli Operasyon Erişimi</div>
              <div class="login-title">TRN sürecinizi tek merkezden yönetin</div>
              <div class="login-copy">Mentor değerlendirmeleri, uçuş bazlı performans kayıtları ve istasyon raporları için rol bazlı erişim.</div>
            </div>
            <div class="login-shield">⌁</div>
          </div>
          <div class="feature-row">
            <div class="feature-chip">✓ Rol Bazlı Yetki</div>
            <div class="feature-chip">✈ Uçuş Bazlı Takip</div>
            <div class="feature-chip">▣ Anlık Raporlama</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    login_tab, signup_tab = st.tabs(["Giriş Yap", "Mentor Hesabı Oluştur"])

    with login_tab:
        role_choice = st.radio("Giriş profili", ["Mentor", "Yetkili / Şef"], horizontal=True, key="login_role_choice")
        if role_choice == "Mentor":
            with st.form("mentor_login"):
                username = st.text_input("Kullanıcı Adı", placeholder="ad.soyad")
                password = st.text_input("Şifre", type="password")
                submitted = st.form_submit_button("Mentor Girişi", type="primary", use_container_width=True)
            if submitted:
                key = username.strip().lower()
                user = st.session_state.users.get(key)
                if user and user["password"] == password:
                    st.session_state.authenticated = True
                    st.session_state.role = "mentor"
                    st.session_state.username = key
                    st.session_state.full_name = user["full_name"]
                    st.toast("Giriş başarılı.", icon="✅")
                    st.rerun()
                else:
                    st.error("Kullanıcı adı veya şifre hatalı.")
            st.markdown('<div class="demo-box"><b>Demo mentor:</b> selin.kaya &nbsp;·&nbsp; <b>Şifre:</b> mentor123</div>', unsafe_allow_html=True)
        else:
            with st.form("admin_login"):
                admin_password = st.text_input("Yetkili / Şef Parolası", type="password")
                submitted = st.form_submit_button("Yetkili Konsoluna Gir", type="primary", use_container_width=True)
            if submitted:
                if admin_password == ADMIN_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.role = "admin"
                    st.session_state.username = "admin"
                    st.session_state.full_name = "Yetkili / Şef"
                    st.toast("Yetkili girişi başarılı.", icon="✅")
                    st.rerun()
                else:
                    st.error("Yetkili parolası hatalı.")
            st.markdown('<div class="demo-box"><b>Demo yetkili parolası:</b> chef2026</div>', unsafe_allow_html=True)

    with signup_tab:
        with st.form("mentor_signup", clear_on_submit=True):
            full_name = st.text_input("Ad Soyad *", placeholder="Ad Soyad")
            new_username = st.text_input("Kullanıcı Adı *", placeholder="ad.soyad")
            c1, c2 = st.columns(2)
            with c1:
                new_password = st.text_input("Şifre *", type="password")
            with c2:
                confirm_password = st.text_input("Şifre Tekrar *", type="password")
            accepted = st.checkbox("Bilgilerimin bu prototip oturumunda saklanmasını kabul ediyorum.")
            created = st.form_submit_button("Mentor Hesabı Oluştur", type="primary", use_container_width=True)
        if created:
            key = new_username.strip().lower()
            if not full_name.strip() or not key or not new_password:
                st.error("Tüm zorunlu alanları doldurun.")
            elif " " in key:
                st.error("Kullanıcı adında boşluk kullanılamaz.")
            elif key in st.session_state.users:
                st.error("Bu kullanıcı adı zaten kayıtlı.")
            elif len(new_password) < 6:
                st.error("Şifre en az 6 karakter olmalıdır.")
            elif new_password != confirm_password:
                st.error("Şifreler eşleşmiyor.")
            elif not accepted:
                st.error("Devam etmek için oturum içi saklama onayını işaretleyin.")
            else:
                st.session_state.users[key] = {"password": new_password, "full_name": full_name.strip()}
                st.success("Mentor hesabı oluşturuldu. Giriş sekmesinden oturum açabilirsiniz.")
    st.markdown('</div>', unsafe_allow_html=True)


# =============================================================================
# MENTOR PANELİ
# =============================================================================
def mentor_panel():
    username = st.session_state.username
    full_name = st.session_state.full_name
    render_header(f"Mentor Paneli · Hoş geldiniz, {full_name}")

    top1, top2, top3 = st.columns([2, 1, 1])
    with top1:
        st.markdown(f'<div class="info-card"><div class="info-label">Aktif Kullanıcı</div><div class="info-value">{full_name}</div><div class="subtle">Mentor yetkisi</div></div>', unsafe_allow_html=True)
    with top2:
        my_count = sum(r["mentor_kullanici"] == username for r in st.session_state.evaluations)
        render_metric("Kayıtlarım", my_count, "Toplam değerlendirme", "#315AAB")
    with top3:
        if st.button("Güvenli Çıkış", use_container_width=True):
            logout()
            st.rerun()

    assigned = [t for t in st.session_state.trainees if t["mentor"] == username]
    if not assigned:
        st.info("Henüz hesabınıza atanmış bir TRN personeli bulunmuyor. Yetkiliyle iletişime geçin.")
        return

    new_tab, history_tab, edit_tab = st.tabs(["＋ Hızlı Uçuş Değerlendirmesi", "Geçmiş Kayıtlarım", "✎ Kayıt Düzenle"])

    with new_tab:
        st.markdown('<div class="section-title">Yeni Operasyon Değerlendirmesi</div>', unsafe_allow_html=True)
        with st.form("new_evaluation", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                trainee_choice = st.selectbox("TRN Personeli *", [trainee_label(t) for t in assigned])
                flight_sequence = st.selectbox("TRN Uçuş Numarası *", list(range(1, 16)), help="İlk 10 uçuş standart süreçtir; gerekirse 11 ve sonrası ek mentörlü uçuş olarak kullanılır.")
                operation_date = st.date_input("Operasyon Tarihi *", value=date.today(), max_value=date.today())
                shift = st.selectbox("Vardiya *", SHIFTS)
                flight = st.selectbox("IST Çıkışlı Uçuş / Uçak *", FLIGHTS)
            with c2:
                duty = st.selectbox("Görev / Eğitim Alanı *", DUTIES)
                counter_no = st.text_input("Kontuar Numarası", placeholder="Örn. B24")
                handled_pax = st.number_input("Personelin İşlem Yaptığı Yolcu", min_value=0, max_value=999, value=10, step=1)
                process_status = st.selectbox("İstasyon Süreç Durumu *", PROCESS_STATUSES)
            note = st.text_area("Detaylı Mentor Değerlendirme Notu *", placeholder="Gözlenen güçlü yönleri ve geliştirilmesi gereken noktaları yazın...", height=110)
            actions = st.text_area("Aksiyon Maddeleri", placeholder="Sonraki uçuşta uygulanacak takip veya eğitim aksiyonları...", height=90)

            with st.expander("01–18 Temel Kontuar Yetkinlikleri", expanded=True):
                st.caption("1: Mentör devralır · 2: Yönlendirmeyle tamamlar · 3: Bağımsız · 4: Üstün bağımsız · G: Gözlemlenmedi")
                basic_scores = {}
                basic_columns = st.columns(2)
                for position, (item_no, description) in enumerate(BASIC_ITEMS.items()):
                    critical_text = " · KRİTİK" if item_no in CRITICAL_ITEMS else ""
                    with basic_columns[position % 2]:
                        basic_scores[item_no] = st.selectbox(
                            f"{item_no}{critical_text} — {description}",
                            SCORE_OPTIONS,
                            index=3,
                            key=f"new_basic_{item_no}",
                        )

            with st.expander("19–26 Özel Durum Yetkinlikleri ve Kanıt", expanded=False):
                st.caption("Kanıt: U gerçek uygulama · S senaryo/simülasyon · T teorik soru-cevap")
                special_scores, special_evidence = {}, {}
                for item_no, description in SPECIAL_ITEMS.items():
                    st.markdown(f"**{item_no} — {description}**")
                    score_col, evidence_col = st.columns([1, 1])
                    with score_col:
                        special_scores[item_no] = st.selectbox("Puan", SCORE_OPTIONS, index=0, key=f"new_special_score_{item_no}")
                    with evidence_col:
                        special_evidence[item_no] = st.selectbox("Kanıt", EVIDENCE_OPTIONS, index=0, key=f"new_special_evidence_{item_no}")

            with st.expander("Geri Bildirim, Kritik Bulgu ve Gelişim Planı", expanded=True):
                f1, f2 = st.columns(2)
                with f1:
                    observation_record = st.text_area("1/2 veya G Maddeleri İçin Somut Gözlem / Eğitim Kaydı", height=100)
                    critical_intervention = st.checkbox("Kritik hata veya mentör müdahalesi var")
                    critical_item_no = st.text_input("Kritik Madde Numarası", placeholder="Örn. 07")
                    prior_finding = st.selectbox("Önceki Açık Bulgu Kontrolü", FINDING_STATUSES)
                    closure_evidence = st.text_area("Kapanış Kanıtı / İşlem Tekrarı", height=80)
                with f2:
                    strong_side = st.text_area("Güçlü Yön", height=80)
                    next_target = st.text_area("Bir Sonraki Uçuş İçin Gelişim Hedefi", height=80)
                    responsible_person = st.text_input("Çalışmayı Yapacak Kişi", value=full_name)
                    target_date = st.date_input("Hedef Uçuş / Tarih", value=date.today() + timedelta(days=3))
                    support_level = st.selectbox("Bu Uçuş Gözlemi", SUPPORT_LEVELS)
                feedback_confirmed = st.checkbox("Geri bildirim personele iletildi ve personel teyidi alındı")
                mentor_confirmed = st.checkbox("Mentör olarak bu uçuş kaydını elektronik biçimde onaylıyorum")
            saved = st.form_submit_button("Değerlendirmeyi Kaydet", type="primary", use_container_width=True)

        if saved:
            metrics_preview = calculate_flight_metrics({"temel_puanlar": basic_scores})
            selected_trainee = next(t for t in assigned if trainee_label(t) == trainee_choice)
            duplicate_flight = any(
                record["trn_sicil"] == selected_trainee["code"]
                and int(record.get("ucus_no", 0)) == int(flight_sequence)
                for record in st.session_state.evaluations
            )
            if len(note.strip()) < 10:
                st.error("Değerlendirme notu en az 10 karakter olmalıdır.")
            elif duplicate_flight:
                st.error(f"{selected_trainee['code']} için {flight_sequence}. uçuş değerlendirmesi zaten kayıtlı. Mevcut kaydı düzenleyin veya farklı uçuş numarası seçin.")
            elif any(special_scores[item_no] != "G" and special_evidence[item_no] == "-" for item_no in SPECIAL_ITEMS):
                st.error("Puanlanan her özel durum için U, S veya T kanıt türü seçilmelidir.")
            elif metrics_preview["critical_low"] and not critical_intervention:
                st.error("Kritik bir maddede 1/2 puan bulundu. Kritik hata veya mentör müdahalesi alanını işaretleyin.")
            else:
                now_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.evaluations.append({
                    "kayit_id": make_record_id(), "zaman_damgasi": now_text,
                    "mentor_kullanici": username, "mentor_ad_soyad": full_name,
                    "trn_sicil": selected_trainee["code"], "trn_ad_soyad": selected_trainee["name"],
                    "operasyon_tarihi": operation_date, "vardiya": shift, "ucus_bilgisi": flight,
                    "gorev_alani": duty, "mentor_puani": round(metrics_preview["average"], 2),
                    "yetkinlik_seviyesi": "Kritik Hata" if metrics_preview["critical_low"] else ("Geliştirilmeli" if metrics_preview["low_items"] else "Başarılı"),
                    "degerlendirme_notu": note.strip(), "aksiyon_maddeleri": actions.strip(),
                    "surec_durumu": process_status, "son_guncelleme": now_text,
                    "ucus_no": flight_sequence,
                    "parkur": flight.split("/")[-1].strip(),
                    "ucak_tipi": flight.split("-")[1].split("/")[0].strip(),
                    "kontuar_no": counter_no.strip(),
                    "islem_yolcu_sayisi": int(handled_pax),
                    "temel_puanlar": basic_scores,
                    "ozel_puanlar": special_scores,
                    "ozel_kanitlar": special_evidence,
                    "gozlem_egitim_kaydi": observation_record.strip(),
                    "kritik_mudahale": critical_intervention,
                    "kritik_madde_no": critical_item_no.strip(),
                    "onceki_bulgu_durumu": prior_finding,
                    "kapanis_kaniti": closure_evidence.strip(),
                    "guclu_yon": strong_side.strip(),
                    "sonraki_hedef": next_target.strip(),
                    "sorumlu_kisi": responsible_person.strip(),
                    "hedef_ucus_tarih": target_date,
                    "destek_seviyesi": support_level,
                    "geri_bildirim_onayi": feedback_confirmed,
                    "mentor_dijital_onay": mentor_confirmed,
                    "mentor_onay_zamani": now_text if mentor_confirmed else "",
                    "personel_onay_zamani": now_text if feedback_confirmed else "",
                })
                selected_trainee["status"] = process_status
                st.toast("Uçuş değerlendirmesi başarıyla kaydedildi.", icon="✅")
                st.rerun()

    with history_tab:
        my_records = [r for r in st.session_state.evaluations if r["mentor_kullanici"] == username]
        if not my_records:
            st.info("Henüz değerlendirme kaydınız bulunmuyor.")
        else:
            st.markdown('<div class="section-title">Değerlendirme Kartlarım</div>', unsafe_allow_html=True)
            render_evaluation_cards(my_records, show_mentor=False)
            st.download_button("Kendi Kayıtlarımı CSV / Excel Uyumlu İndir", data=csv_bytes(my_records), file_name=f"mentor_degerlendirmeleri_{username}_{date.today():%Y%m%d}.csv", mime="text/csv", use_container_width=True)

    with edit_tab:
        my_records = [r for r in st.session_state.evaluations if r["mentor_kullanici"] == username]
        if not my_records:
            st.info("Düzenlenebilecek kayıt bulunmuyor.")
        else:
            options = {f"{r['operasyon_tarihi']:%d.%m.%Y} · {r['trn_sicil']} · {r['ucus_bilgisi']} · {r['kayit_id']}": r for r in sorted(my_records, key=lambda x: x["zaman_damgasi"], reverse=True)}
            selected_label = st.selectbox("Düzenlenecek Kayıt", list(options.keys()))
            selected = options[selected_label]
            with st.form("edit_evaluation"):
                edit_status = st.selectbox("Süreç Durumu", PROCESS_STATUSES, index=PROCESS_STATUSES.index(selected["surec_durumu"]))
                edit_note = st.text_area("Değerlendirme Notu", value=selected["degerlendirme_notu"], height=110)
                edit_actions = st.text_area("Aksiyon Maddeleri", value=selected["aksiyon_maddeleri"], height=90)
                with st.expander("01–18 Temel Yetkinlik Puanlarını Düzenle"):
                    edit_basic = {}
                    edit_cols = st.columns(2)
                    for position, (item_no, description) in enumerate(BASIC_ITEMS.items()):
                        current = str(selected.get("temel_puanlar", {}).get(item_no, "G"))
                        with edit_cols[position % 2]:
                            edit_basic[item_no] = st.selectbox(
                                f"{item_no} — {description}", SCORE_OPTIONS,
                                index=SCORE_OPTIONS.index(current), key=f"edit_basic_{selected['kayit_id']}_{item_no}",
                            )
                with st.expander("19–26 Özel Durum Puan ve Kanıtlarını Düzenle"):
                    edit_special, edit_evidence = {}, {}
                    for item_no, description in SPECIAL_ITEMS.items():
                        st.markdown(f"**{item_no} — {description}**")
                        score_col, evidence_col = st.columns(2)
                        current_score = str(selected.get("ozel_puanlar", {}).get(item_no, "G"))
                        current_evidence = str(selected.get("ozel_kanitlar", {}).get(item_no, "-"))
                        with score_col:
                            edit_special[item_no] = st.selectbox(
                                "Puan", SCORE_OPTIONS, index=SCORE_OPTIONS.index(current_score),
                                key=f"edit_special_score_{selected['kayit_id']}_{item_no}",
                            )
                        with evidence_col:
                            edit_evidence[item_no] = st.selectbox(
                                "Kanıt", EVIDENCE_OPTIONS, index=EVIDENCE_OPTIONS.index(current_evidence),
                                key=f"edit_special_evidence_{selected['kayit_id']}_{item_no}",
                            )
                with st.expander("Geri Bildirim ve Gelişim Planını Düzenle"):
                    edit_observation = st.text_area("Somut Gözlem / Eğitim Kaydı", value=selected.get("gozlem_egitim_kaydi", ""), height=90)
                    edit_closure = st.text_area("Kapanış Kanıtı", value=selected.get("kapanis_kaniti", ""), height=80)
                    edit_strong = st.text_area("Güçlü Yön", value=selected.get("guclu_yon", ""), height=70)
                    edit_target = st.text_area("Sonraki Uçuş Hedefi", value=selected.get("sonraki_hedef", ""), height=70)
                    current_support = selected.get("destek_seviyesi", SUPPORT_LEVELS[0])
                    edit_support = st.selectbox("Destek Seviyesi", SUPPORT_LEVELS, index=SUPPORT_LEVELS.index(current_support))
                    edit_feedback = st.checkbox("Geri bildirim personele iletildi ve personel teyidi alındı", value=bool(selected.get("geri_bildirim_onayi")))
                    edit_mentor_confirmation = st.checkbox("Mentör elektronik onayı", value=bool(selected.get("mentor_dijital_onay")))
                updated = st.form_submit_button("Değişiklikleri Kaydet", type="primary", use_container_width=True)
            if updated:
                if len(edit_note.strip()) < 10:
                    st.error("Değerlendirme notu en az 10 karakter olmalıdır.")
                elif any(edit_special[item_no] != "G" and edit_evidence[item_no] == "-" for item_no in SPECIAL_ITEMS):
                    st.error("Puanlanan her özel durum için U, S veya T kanıt türü seçilmelidir.")
                else:
                    edited_metrics = calculate_flight_metrics({"temel_puanlar": edit_basic})
                    selected["temel_puanlar"] = edit_basic
                    selected["ozel_puanlar"] = edit_special
                    selected["ozel_kanitlar"] = edit_evidence
                    selected["mentor_puani"] = round(edited_metrics["average"], 2)
                    selected["yetkinlik_seviyesi"] = "Kritik Hata" if edited_metrics["critical_low"] else ("Geliştirilmeli" if edited_metrics["low_items"] else "Başarılı")
                    selected["surec_durumu"] = edit_status
                    selected["degerlendirme_notu"] = edit_note.strip()
                    selected["aksiyon_maddeleri"] = edit_actions.strip()
                    selected["gozlem_egitim_kaydi"] = edit_observation.strip()
                    selected["kapanis_kaniti"] = edit_closure.strip()
                    selected["guclu_yon"] = edit_strong.strip()
                    selected["sonraki_hedef"] = edit_target.strip()
                    selected["destek_seviyesi"] = edit_support
                    selected["geri_bildirim_onayi"] = edit_feedback
                    selected["mentor_dijital_onay"] = edit_mentor_confirmation
                    update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    selected["mentor_onay_zamani"] = update_time if edit_mentor_confirmation else ""
                    selected["personel_onay_zamani"] = update_time if edit_feedback else ""
                    selected["son_guncelleme"] = update_time
                    st.toast("Kayıt güncellendi.", icon="✅")
                    st.rerun()


# =============================================================================
# YETKİLİ / ŞEF KONSOLU
# =============================================================================
def admin_console():
    render_header("Yetkili / Şef Konsolu · Tüm istasyon eğitim performansının merkezi görünümü")
    records = st.session_state.evaluations
    exit_col, spacer = st.columns([1, 4])
    with exit_col:
        if st.button("Güvenli Çıkış", use_container_width=True):
            logout()
            st.rerun()

    unique_trainees = {r["trn_sicil"] for r in records}
    critical_count = sum(r["yetkinlik_seviyesi"] == "Kritik Hata" or int(r["mentor_puani"]) <= 1 for r in records)
    flight_counts = pd.Series([r["trn_ad_soyad"] for r in records]).value_counts() if records else pd.Series(dtype=int)
    leader = flight_counts.index[0] if not flight_counts.empty else "—"
    leader_count = int(flight_counts.iloc[0]) if not flight_counts.empty else 0

    kpi_cols = st.columns(4)
    kpis = [
        ("Toplam Değerlendirme", len(records), "Tüm kayıtlar", "#315AAB"),
        ("Aktif TRN", len(unique_trainees), "Değerlendirilen personel", "#FFAC00"),
        ("Kritik Not", critical_count, "Acil takip gerektiren", "#C93F49"),
        ("En Çok Uçuşa Giren", leader, f"{leader_count} değerlendirme", "#16845B"),
    ]
    for col, item in zip(kpi_cols, kpis):
        with col:
            render_metric(*item)

    dashboard_tab, readiness_tab, audit_tab, tools_tab = st.tabs(["Analitik & Filtreler", "10 Uçuş & Nihai Öneri", "Denetim Tablosu", "Yönetim Araçları"])

    with dashboard_tab:
        st.markdown('<div class="section-title">Gelişmiş Filtreleme</div>', unsafe_allow_html=True)
        mentor_names = sorted({r["mentor_ad_soyad"] for r in records})
        trainee_names = sorted({f"{r['trn_sicil']} - {r['trn_ad_soyad']}" for r in records})
        flight_names = sorted({r["ucus_bilgisi"] for r in records})
        f1, f2, f3 = st.columns(3)
        with f1:
            search = st.text_input("Anlık Arama", placeholder="Mentor, sicil, personel, uçuş...")
            selected_mentors = st.multiselect("Mentor", mentor_names)
        with f2:
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
                ("Geri bildirim ve teyitler tamam", readiness["feedback_complete"]),
                ("Eğitim, süre ve yetki koşulları", readiness["external_conditions_ready"]),
            ]
            check_html = "".join(
                f'<span class="pill {"good" if passed else "warn"}">{"✓" if passed else "○"} {safe_html(label)}</span> '
                for label, passed in checks
            )
            st.markdown(
                f'<div class="evaluation-card" style="--card-accent:{accent}">'
                f'<div class="evaluation-head"><div><div class="evaluation-name">{safe_html(trainee_label(trainee))}</div>'
                f'<div class="evaluation-id">Mentor: {safe_html(st.session_state.users.get(trainee["mentor"], {}).get("full_name", trainee["mentor"]))} · '
                f'Son iki uçuş: {safe_html(", ".join(map(str, readiness["last_two_flights"])) or "—")}</div></div>'
                f'<div class="score-circle">{min(readiness["flight_count"], 10)}/10</div></div>'
                f'<div class="evaluation-grid"><div><div class="evaluation-label">Sınıf Eğitimi Bitişi</div><div class="evaluation-value">{trainee["class_end"]:%d.%m.%Y}</div></div>'
                f'<div><div class="evaluation-label">TRN Başlangıcı</div><div class="evaluation-value">{trainee["trn_start"]:%d.%m.%Y}</div></div>'
                f'<div><div class="evaluation-label">Yetkili Karar</div><div class="evaluation-value">{safe_html(readiness["authorized_decision"])}</div></div>'
                f'<div><div class="evaluation-label">Ön Koşul Kaydı</div><div class="evaluation-value">{safe_html(trainee.get("prerequisites", "—"))}</div></div></div>'
                f'<div class="note-box"><b>{safe_html(recommendation)}</b><br>{check_html}</div></div>',
                unsafe_allow_html=True,
            )
            trainee_records = [r for r in records if r["trn_sicil"] == trainee["code"]]
            if trainee_records:
                with st.expander(f"{trainee['code']} uçuş kayıtlarını aç"):
                    render_evaluation_cards(trainee_records, show_mentor=True)

        st.markdown('<div class="section-title">Mentör Önerisi ve Yetkili Kararı</div>', unsafe_allow_html=True)
        decision_labels = {trainee_label(item): item for item in st.session_state.trainees}
        decision_label = st.selectbox("Nihai değerlendirme yapılacak TRN personeli", list(decision_labels))
        decision_trainee = decision_labels[decision_label]
        existing_decision = st.session_state.final_decisions.get(decision_trainee["code"], {})
        with st.form(f"final_decision_{decision_trainee['code']}"):
            d1, d2 = st.columns(2)
            with d1:
                mentor_recommendation = st.selectbox(
                    "Mentör Önerisi",
                    MENTOR_RECOMMENDATIONS,
                    index=MENTOR_RECOMMENDATIONS.index(existing_decision.get("mentor_onerisi", MENTOR_RECOMMENDATIONS[0])),
                )
                authorized_decision = st.selectbox(
                    "Yetkili Karar",
                    AUTHORIZED_DECISIONS,
                    index=AUTHORIZED_DECISIONS.index(existing_decision.get("yetkili_karar", AUTHORIZED_DECISIONS[0])),
                )
                external_conditions = st.checkbox(
                    "Güncel eğitim, asgari süre ve taşıyıcı yetkilendirme koşulları tamamlandı",
                    value=bool(existing_decision.get("egitim_sure_yetki_tamam")),
                )
                planning_start = st.date_input(
                    "Planlamaya Esas Başlangıç Tarihi",
                    value=existing_decision.get("planlama_baslangic", date.today()),
                )
            with d2:
                carrier_approval = st.text_input("Taşıyıcı Release / Onay Kayıt No", value=existing_decision.get("tasiyici_onay_no", ""))
                scope = st.text_area("Görev Kapsamı ve Yetki Sınırı", value=existing_decision.get("gorev_kapsami", ""), height=80)
                justification = st.text_area("Gerekçe / Ek Uçuş Hedefi / Destek Düzeni", value=existing_decision.get("gerekce", ""), height=80)
            s1, s2, s3 = st.columns(3)
            with s1:
                mentor_signer = st.text_input("Mentör Adı Soyadı", value=existing_decision.get("mentor_imza", ""))
            with s2:
                manager_signer = st.text_input("Birim Yöneticisi Adı Soyadı", value=existing_decision.get("yonetici_imza", st.session_state.full_name or ""))
            with s3:
                carrier_official = st.text_input("Taşıyıcı Yetkilisi / Onay Kaydı", value=existing_decision.get("tasiyici_yetkilisi", ""))
            planning_notified = st.text_input("Planlama Birimine Bildiren", value=existing_decision.get("planlamaya_bildiren", ""))
            final_confirmation = st.checkbox(
                "Yetkili olarak bu nihai değerlendirme kaydını elektronik biçimde onaylıyorum",
                value=bool(existing_decision.get("yetkili_dijital_onay")),
            )
            save_decision = st.form_submit_button("Nihai Kararı Kaydet / Güncelle", type="primary", use_container_width=True)
        if save_decision:
            decision_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            selected_readiness = calculate_trainee_readiness(decision_trainee["code"])
            approval_blocked = (
                authorized_decision == "Tek başına planlama onaylandı"
                and (not selected_readiness["technical_ready"] or not external_conditions)
            )
            if approval_blocked:
                st.error("Tek başına planlama onayı verilemez: 10 uçuş, son iki uçuş, özel durum, açık bulgu veya teyit koşullarından en az biri tamamlanmamış.")
            elif final_confirmation and not manager_signer.strip():
                st.error("Elektronik nihai onay için birim yöneticisi adı soyadı zorunludur.")
            else:
                st.session_state.final_decisions[decision_trainee["code"]] = {
                "mentor_onerisi": mentor_recommendation,
                "yetkili_karar": authorized_decision,
                "egitim_sure_yetki_tamam": external_conditions,
                "gerekce": justification.strip(),
                "gorev_kapsami": scope.strip(),
                "planlama_baslangic": planning_start,
                "tasiyici_onay_no": carrier_approval.strip(),
                "mentor_imza": mentor_signer.strip(),
                "yonetici_imza": manager_signer.strip(),
                "tasiyici_yetkilisi": carrier_official.strip(),
                "planlamaya_bildiren": planning_notified.strip(),
                "yetkili_dijital_onay": final_confirmation,
                "yetkili_onay_zamani": decision_time if final_confirmation else "",
                "son_guncelleme": decision_time,
                }
                st.toast("Nihai değerlendirme kaydı güncellendi.", icon="✅")
                st.rerun()

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
        t1, t2, t3 = st.columns(3)
        with t1:
            st.download_button("Tüm Değerlendirme Raporunu İndir", data=csv_bytes(records), file_name=f"istasyon_trn_tum_rapor_{date.today():%Y%m%d}.csv", mime="text/csv", use_container_width=True)
        with t2:
            st.download_button("Gelişim ve Nihai Karar Raporunu İndir", data=final_csv_bytes(), file_name=f"istasyon_trn_nihai_karar_{date.today():%Y%m%d}.csv", mime="text/csv", use_container_width=True)
        with t3:
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

st.caption("İstasyon TRN Portalı · Operasyonel prototip · Veriler aktif oturumda saklanır")
