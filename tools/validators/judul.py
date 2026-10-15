"""Validator mutu judul (kerangka JD1-JD6).

Memeriksa **setiap** judul yang ditegakkan di repositori ini:

- setiap catatan pada ``research/judul.json`` (bidang ``judul``);
- setiap ``title:`` pada ``templates/artikel-*-meta.yaml`` (placeholder dilewati);
- judul skripsi pada ``content/skripsi/00-halaman-judul.md``.

Enam aturan absolut (lihat ``docs/judul-framework.md``):

- **JD1** judul direktif: memuat >= 1 penanda aksi/tujuan (``judul_verba_aksi``).
- **JD2** lingkup terkendali: <= 2 penanda lingkup, <= 1 wilayah/venue,
  <= 1 rentang waktu.
- **JD3** menyatakan masalah atau solusi/kontribusi: memuat >= 1 penanda
  masalah (``judul_penanda_masalah``) atau solusi (``judul_penanda_solusi``).
- **JD4** panjang judul dalam pita 6-16 kata.
- **JD5** bukan bentuk tanya dan tanpa penanda kabur (``judul_terlarang``).
- **JD6** bahasa konsisten: seluruhnya Indonesia atau seluruhnya Inggris.

Registri dibaca dari ``assets/bahasa/kamus-id.yaml`` bagian ``judul``. Lapisan
opsional tinjauan agen hanya aktif dengan ``--agent``.
"""

import glob
import json
import os
import re
import unicodedata

import yaml

from .base import Context, Finding, read, register

KAMUS = "assets/bahasa/kamus-id.yaml"
JUDUL_JSON = "research/judul.json"
ARTIKEL_GLOB = "templates/artikel-*-meta.yaml"
HALAMAN_JUDUL = "content/skripsi/00-halaman-judul.md"

# Pita panjang judul (JD4), dikalibrasi pada korpus Sinta (min 4, maks 16,
# median 7) dan pita dokumen `<=12-16`; lihat docs/judul-framework.md §6.
PANJANG_MIN = 6
PANJANG_MAKS = 16

# Ambang lingkup (JD2), dikalibrasi pada korpus Sinta (maks teramati = 2).
LINGKUP_MAKS = 2
WILAYAH_MAKS = 1
WAKTU_MAKS = 1

# Placeholder judul artikel yang harus dilewati.
PLACEHOLDER = ("Judul Artikel", "≤", "<", "…")

# Deteksi bahasa (JD6): kata fungsi + kata khas-judul yang ejaannya berbeda
# antar bahasa. Kedua himpunan harus saling lepas (disjoint) agar kata serapan
# yang sama ejaannya (mis. "model", "data", "global") tidak memicu positif palsu.
KATA_FUNGSI_ID = {
    "dan", "atau", "yang", "untuk", "dengan", "pada", "dalam", "di", "ke",
    "dari", "terhadap", "melalui", "oleh", "sebagai", "adalah", "ini", "itu",
    "tahun", "masa", "antara", "serta", "bagi", "atas", "bawah", "selama",
    "hingga", "sampai", "para", "suatu", "sebuah", "tidak", "bukan", "akan",
    "telah", "sudah", "dapat", "bisa", "juga", "masih", "agar", "kepada",
    "tentang", "secara", "guna", "maupun", "namun", "yaitu",
}
KATA_FUNGSI_EN = {
    "the", "a", "an", "of", "in", "on", "at", "to", "for", "with", "by",
    "from", "and", "or", "as", "into", "over", "under", "between", "during",
    "through", "using", "across", "this", "that", "these", "those", "its",
    "their", "is", "are", "was", "were", "be", "been", "being", "toward",
    "towards", "against", "among", "within", "without", "via", "per",
}
# Kata khas-judul (ejaan berbeda ID vs EN) untuk menangkap judul campuran yang
# kata fungsinya hanya muncul di satu bahasa.
KATA_KHAS_ID = {
    "analisis", "strategi", "pengaruh", "dampak", "peran", "evaluasi",
    "penerapan", "implementasi", "pengembangan", "perbandingan", "kajian",
    "studi", "optimalisasi", "peningkatan", "efektivitas", "efisiensi",
    "diplomasi", "vaksin", "kebijakan", "pemasaran", "ekspor", "impor",
    "citra", "negara", "bangsa", "publik", "masyarakat", "ekonomi", "politik",
    "hukum", "pendidikan", "kesehatan", "pariwisata", "pertumbuhan",
    "ketimpangan", "kesenjangan", "tantangan", "kerangka", "pendekatan",
    "rekomendasi", "inovasi", "wilayah", "daerah", "pasar", "industri",
    "perusahaan", "organisasi", "manajemen", "teknologi", "sistem",
    "informasi", "sosial", "budaya", "internasional", "kinerja", "prediksi",
    "klasifikasi", "tujuan", "manfaat", "metode", "penelitian", "hasil",
}
KATA_KHAS_EN = {
    "analysis", "strategy", "effect", "impact", "role", "evaluation",
    "implementation", "development", "comparison", "review", "study",
    "optimization", "improvement", "effectiveness", "efficiency", "diplomacy",
    "vaccine", "policy", "marketing", "export", "import", "image", "nation",
    "state", "public", "society", "economy", "politics", "law", "education",
    "health", "tourism", "growth", "inequality", "challenge", "framework",
    "approach", "recommendation", "innovation", "region", "market", "industry",
    "company", "organization", "management", "technology", "system",
    "information", "social", "culture", "international", "performance",
    "prediction", "classification", "objective", "benefit", "method",
    "research", "results",
}
STOPWORD_ID = KATA_FUNGSI_ID | KATA_KHAS_ID
STOPWORD_EN = KATA_FUNGSI_EN | KATA_KHAS_EN


def _kamus(ctx: Context) -> dict:
    with open(os.path.join(ctx.root, KAMUS), encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _norm(text: str) -> str:
    """Lipat-ASCII, huruf kecil, non-alfanumerik -> spasi (untuk pencocokan)."""
    folded = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode("ascii")
    folded = folded.lower()
    folded = re.sub(r"[^a-z0-9]+", " ", folded)
    return folded.strip()


def _marker_re(marker: str) -> re.Pattern:
    return re.compile(r"(?<![a-z0-9])" + re.escape(_norm(marker)) + r"(?![a-z0-9])")


def _hits(text: str, markers: list[str]) -> list[str]:
    """Penanda yang muncul >= 1 kali di ``text`` (dedup, urut sesuai daftar)."""
    out: list[str] = []
    for m in markers:
        nm = _norm(m)
        if nm and _marker_re(m).search(text):
            out.append(m)
    return out


def _count(text: str, markers: list[str]) -> int:
    """Total kemunculan penanda (termasuk penanda yang beririsan)."""
    total = 0
    for m in markers:
        nm = _norm(m)
        if nm:
            total += len(_marker_re(m).findall(text))
    return total


def _timeframes(raw: str) -> int:
    """Banyak rentang waktu berbeda: satu tahun tunggal atau satu rentang."""
    low = raw.lower().replace("–", "-").replace("—", "-").replace("−", "-")
    spans = 0
    covered: set[str] = set()
    for m in re.finditer(r"\b((?:19|20)\d{2})\s*-\s*((?:19|20)\d{2})\b", low):
        spans += 1
        covered.update(m.groups())
    for m in re.finditer(r"\b((?:19|20)\d{2})\b", low):
        if m.group(1) not in covered:
            spans += 1
    return spans


def _bahasa(text: str) -> str:
    """Tebak bahasa judul: ``id``, ``en``, ``mixed``, atau ``?`` (netral).

    Kata fungsi adalah sinyal kuat; kata khas-judul (sering dipinjam sebagai
    istilah asing) adalah sinyal lemah. Judul dinilai ``mixed`` bila:
    (a) kedua bahasa muncul pada kata fungsi; (b) kata fungsi satu bahasa
    muncul bersama >= 2 kata khas bahasa lain; atau (c) kedua bahasa
    menyumbang >= 2 kata khas masing-masing (mis. ``Analisis Strategi vaccine
    diplomacy Tiongkok`` yang tanpa kata fungsi).
    """
    tokens = _norm(text).split()
    id_f = sum(1 for t in tokens if t in KATA_FUNGSI_ID)
    en_f = sum(1 for t in tokens if t in KATA_FUNGSI_EN)
    id_c = sum(1 for t in tokens if t in KATA_KHAS_ID)
    en_c = sum(1 for t in tokens if t in KATA_KHAS_EN)
    if id_f and en_f:
        return "mixed"
    if id_f and en_c >= 2:
        return "mixed"
    if en_f and id_c >= 2:
        return "mixed"
    if id_c >= 2 and en_c >= 2:
        return "mixed"
    if id_f:
        return "id"
    if en_f:
        return "en"
    return "?"


def _strip_latex(text: str) -> str:
    text = re.sub(r"\\[a-zA-Z]+\*?", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    return " ".join(text.split())


def _judul_skripsi(ctx: Context) -> str | None:
    text = read(HALAMAN_JUDUL)
    if text is None:
        return None
    m = re.search(r"\\bfseries\s+(?P<t>.+?)\\par", text, re.DOTALL)
    if not m:
        return None
    return _strip_latex(m.group("t"))


def _judul_json(ctx: Context, findings: list[Finding]) -> list[tuple[str, str]]:
    text = read(JUDUL_JSON)
    if text is None:
        findings.append(Finding("warn", f"{JUDUL_JSON} belum ada"))
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        findings.append(Finding("fail", f"{JUDUL_JSON} bukan JSON valid"))
        return []
    if not isinstance(data, list):
        findings.append(Finding("fail", f"{JUDUL_JSON} bukan array JSON"))
        return []
    out: list[tuple[str, str]] = []
    for rec in data:
        if not isinstance(rec, dict):
            continue
        title = rec.get("judul")
        if not isinstance(title, str) or not title.strip():
            continue
        rid = rec.get("id") or "?"
        out.append((f"{JUDUL_JSON}:{rid}", title.strip()))
    return out


def _judul_artikel(ctx: Context) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for path in sorted(glob.glob(os.path.join(ctx.root, ARTIKEL_GLOB))):
        rel = os.path.relpath(path, ctx.root)
        text = read(rel)
        if text is None:
            continue
        try:
            meta = yaml.safe_load(text) or {}
        except yaml.YAMLError:
            continue
        title = meta.get("title") if isinstance(meta, dict) else None
        if not isinstance(title, str) or not title.strip():
            continue
        if any(p in title for p in PLACEHOLDER):
            continue
        out.append((rel, title.strip()))
    return out


def _periksa(label: str, title: str, vocab: dict, findings: list[Finding]) -> None:
    norm = _norm(title)
    words = len(title.split())
    aksi = vocab.get("judul_verba_aksi") or []
    lingkup = vocab.get("judul_penanda_lingkup") or []
    wilayah = vocab.get("judul_penanda_wilayah") or []
    masalah = vocab.get("judul_penanda_masalah") or []
    solusi = vocab.get("judul_penanda_solusi") or []
    terlarang = vocab.get("judul_terlarang") or []

    # --- JD1: judul direktif ---
    if not _hits(norm, aksi):
        findings.append(Finding(
            "fail", f"{label}: JD1: judul tanpa penanda aksi/tujuan"))

    # --- JD2: lingkup terkendali ---
    n_lingkup = _count(norm, lingkup)
    if n_lingkup > LINGKUP_MAKS:
        findings.append(Finding(
            "fail", f"{label}: JD2: penanda lingkup {n_lingkup} > "
                    f"{LINGKUP_MAKS} (lingkup terlalu luas)"))
    n_wilayah = _count(norm, wilayah)
    if n_wilayah > WILAYAH_MAKS:
        findings.append(Finding(
            "fail", f"{label}: JD2: wilayah/venue {n_wilayah} > {WILAYAH_MAKS}"))
    n_waktu = _timeframes(title)
    if n_waktu > WAKTU_MAKS:
        findings.append(Finding(
            "fail", f"{label}: JD2: rentang waktu {n_waktu} > {WAKTU_MAKS}"))

    # --- JD3: masalah atau solusi/kontribusi ---
    m_hits = _hits(norm, masalah)
    s_hits = _hits(norm, solusi)
    if not m_hits and not s_hits:
        findings.append(Finding(
            "fail", f"{label}: JD3: judul tanpa penanda masalah maupun "
                    f"solusi/kontribusi"))

    # --- JD4: panjang judul dalam pita ---
    if not (PANJANG_MIN <= words <= PANJANG_MAKS):
        findings.append(Finding(
            "fail", f"{label}: JD4: {words} kata di luar pita "
                    f"{PANJANG_MIN}-{PANJANG_MAKS}"))

    # --- JD5: bukan bentuk tanya & tanpa penanda kabur ---
    if "?" in title:
        findings.append(Finding("fail", f"{label}: JD5: judul berbentuk tanya"))
    kabur = _hits(norm, terlarang)
    if kabur:
        findings.append(Finding(
            "fail", f"{label}: JD5: penanda kabur: {', '.join(kabur)}"))

    # --- JD6: bahasa konsisten ---
    lang = _bahasa(title)
    if lang == "mixed":
        findings.append(Finding(
            "fail", f"{label}: JD6: judul campuran Indonesia-Inggris"))


@register("judul", "research/judul.json + templates/artikel-*-meta.yaml + "
                   "content/skripsi/00-halaman-judul.md (JD1-JD6)")
def run(ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    vocab = (_kamus(ctx).get("judul") or {})

    judul: list[tuple[str, str]] = []
    judul.extend(_judul_json(ctx, findings))
    judul.extend(_judul_artikel(ctx))
    skripsi = _judul_skripsi(ctx)
    if skripsi:
        judul.append((HALAMAN_JUDUL, skripsi))
    elif read(HALAMAN_JUDUL) is not None:
        findings.append(Finding(
            "fail", f"{HALAMAN_JUDUL}: judul skripsi tidak terbaca"))

    for label, title in judul:
        _periksa(label, title, vocab, findings)

    # Lapisan opsional tinjauan agen (hanya dengan --agent).
    if ctx.agent:
        for label, title in judul:
            claims = [
                f"Judul '{title}' menyatakan masalah yang diteliti atau "
                f"kontribusi/solusi yang ditawarkan.",
                f"Judul '{title}' bersifat direktif (memuat tindakan/tujuan "
                f"penelitian), bukan sekadar topik.",
            ]
            findings.extend(ctx.agent_review("judul", claims, f"{label}: {title}"))

    if not any(f.level == "fail" for f in findings):
        findings.append(Finding(
            "ok", f"judul patuh kerangka JD1-JD6 ({len(judul)} judul diperiksa)"))
    return findings
