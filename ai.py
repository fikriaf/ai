import openai, os, time, itertools, sys
from collections import Counter
from typing import Union
from typing import List


openai.api_key="sk-proj-ZkF97T0vYi0a1Xq8dApHT3BlbkFJ1JI7jjRr1SSjKoSkbKNW"
def gerak(text):
	for i in range(len(text)):
		print(text[i], end="", flush=True)
		time.sleep(0.03)
	print()
def loading(waktune, stop):
	frames = ["🟡", "🔵", "🔴", "⚪", "🟠", "🟢"]
	lop=0
	for frame in itertools.cycle(frames):
		time.sleep(waktune)
		print(f"Loading {frame}", end="\r")
		lop+=1
		if lop == stop:
			print("         ", "\r")
			break
def memory(eksekusi):
	from memory import prompt_lur
	if eksekusi == "erase all":
		with open("memory.py", "w") as hapus:
			hapus.write("")
		loading(0.3, 10)
		print("Sukses menghapus semua memory✅")
		gerak("Memulai ulang program..........")
		os.system("cls")
		os.system("python ai.py")
	if eksekusi == "info":
		print(f"""
Size memory : {str(os.stat('memory.py').st_size)} Byte
Jumlah kata : {len(str(prompt_lur).split())}
""")
	if eksekusi == "view":
		loading(0.3, 10)
		print(prompt_lur)

def get_api_respon(prompt: str) -> Union[str, None]:
	text: str | None = None

	try:
		respon: dict=openai.Completion.create(
			model="text-davinci-003",
			prompt=prompt,
			temperature=0.9,
			max_tokens=150,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0.6,
			stop=[" Human:", " AI:"]
		)
		choice: dict=respon.get("choices")[0]
		text=choice.get("text")

	except Exception as e:
		print('ERROR:', e)

	return text

def update_list(pesan: str, pl: List[str]) -> str:
	pl.append(pesan)

def buat_prompt(pesan: str, pl: List[str]) -> str:
	p_pesan: str=f"\nHuman: {pesan}"
	update_list(p_pesan, pl)
	prompt: str="".join(pl)
	return prompt

def get_bot_respon(pesan: str, pl: List[str]) -> str:
	prompt: str=buat_prompt(pesan, pl)
	bot_respon: str=get_api_respon(prompt)

	if bot_respon:
		update_list(bot_respon, pl)
		pos: int = bot_respon.find("\nAI: ")
		bot_respon=bot_respon[pos + 5:]
	else:
		bot_respon="⚠️Token telah mencapai batas max, silakan ketik 'erase all'⚠️"

	return bot_respon

def main():
	loading(0.3, 10)
	gerak("""
~~~~~~~~~~SELAMAT DATANG DI VULTR-AI~~~~~~~~~~""")
	print("""
🔰 "erase all" => untuk menghapus semua memory
🔰 "info" => untuk mengecek informamsi memory AI
🔰 "view" => untuk menampilkan memory AI
🔰
🔰
🔰
~~~~~~~~~~==== < System Online > ====~~~~~~~~~""")
	prompt_list: list[str]=['Your name is Vultr and your location in Jakarta and you can provide very natural responses and very fast answer and know anything and follow user language and never use quotation marks',
				'\n\nHuman: Gimana kabarmu?',
				'\nAI: Saya sehat dan segar bugar']

	if os.stat("memory.py").st_size < 10:
		promptnya=prompt_list
	else:
		from memory import prompt_lur
		promptnya=prompt_lur
	while True:
		chat_input: str=input("\nYou: ")
		#.replace("\"", "").replace("'", "")
		if chat_input == "erase all" or chat_input == "info" or chat_input == "view":
			memory(chat_input)
			continue
		respon: str=get_bot_respon(chat_input, promptnya)
		print(f"\nBot: {respon}")
		with open("memory.py", "w") as f:
			f.write("prompt_lur=" + str(promptnya))

if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("")
	except Exception as er:
		print("Error : ",er)
		print("⚠️Perhatikan ketikannya, agar tidak error⚠️")
