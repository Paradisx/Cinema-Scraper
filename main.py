import os, sys, requests
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed

white = "\x1b[0m"
pink = "\x1b[38;5;218m"
logo = f"""\t\t\t{pink} ┌┼┐  {white}╔═╗╦╔╗╔╔═╗╔╦╗╔═╗  {pink}┌┼┐\n\t\t\t{pink} └┼┐  {white}║  ║║║║║╣ ║║║╠═╣  {pink}└┼┐\n\t\t\t{pink} └┼┘  {white}╚═╝╩╝╚╝╚═╝╩ ╩╩ ╩  {pink}└┼┘\n\n"""

def Main():
    os.system('cls && title [Cinema Scraper] & mode 80,24')
    print(logo)
    wb = input(f"{white}[{pink}?{white}] Webhook Link{pink}?{white}")
    url = input(f"{white}[{pink}?{white}] Link To Scrape{pink}?{white}")
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    soup = BeautifulSoup(r.content, "html.parser")
    images = soup.find_all('img')
    images = images[3:-1]
    x = 0
    for a in images:
     Link = a.attrs.get("src")
     hook = Webhook(wb)
     embed=Embed(color=0xffb2fd,timestamp='now')
     embed.set_author(name="Cinema Scraper",icon_url=Link)
     embed.set_image(Link)
     embed.set_footer(text=f'Made By Ashley❤️')
     hook.send(embed=embed)
     x += 1
     total  = len(images)
     os.system('cls')
     sys.stdout.write('\r'+logo+f'\t\t\t     {pink}[{white}!{pink}]{white} Sent {pink}[{white}{x}/{total}{pink}]')
     sys.stdout.flush()
    os.system("pause >NUL")
    Main()

if __name__ == '__main__':
    Main()
