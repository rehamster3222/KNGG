from PIL import Image, ImageDraw, ImageFont
import qrcode, os, random


zvdscp = 0
zvezd = 0
neutronzvezd = 0
planets = 0
asteroids = 0
blackholesv = 0
blackhole = 0
zvezdscpl = 0
kvz = 0
puls = 0
magn = 0

oldir = os.getcwd()

def galaxies(seedf: int, seedt: int):
	global zvezd,neutronzvezd,planets,asteroids,blackholesv,blackhole,zvezdscpl,kvz,puls,magn,zvdscp
	random.seed(seedf)
	os.chdir(oldir)
	os.makedirs("galaxies", exist_ok=True)
	os.chdir("galaxies")
	glxx = random.choice(["NGC", "MGC", "JGC"])
	gllx = random.randint(1000, 9999)
	galx = (f"{glxx}{gllx}")
	with open(
	f"galaxy-{galx}.txt", "a"
	) as ksm:
		ksm.write(f"Галактика {galx}")
		ksm.write(f"\nKNGG Generator")
		ksm.write(f"\nсистем: {seedt}")
		shnc = random.uniform(0, 1)
		bhc = random.uniform(0, 1)
		for ct in range (seedt):
			
			#st
			asss = random.uniform(0.01, 50)
			aosh = random.uniform(0, 1)
			aon = random.choice(["Пелея", "Мирра", "Глаз Вселенной", "Лея", "Страннкик"])
			aoy = random.uniform(-10999999, 10999999)
			aox = random.uniform(-12999999, 129999999)
			aoz = random.uniform(-9999999, 9999999)
			aossx = random.uniform(-1250, 1250)
			aossy = random.uniform(-1250, 1250)
			aossz = random.uniform(-1250, 1250)
			
			aot = random.uniform(0, 1)
			amsh = random.randint(1, 4)
			stm = random.uniform(0.01, 600)
			stl = random.uniform(100, 2500)
			stn = random.randint(100, 30000)
			stt = random.randint(1000, 42000)
			ste = random.uniform(0.01, 13.8)
			aott = random.randint(1, 3)
			if aot < 0.30:
				sty = random.uniform(-10999999, 10999999)
				stx = random.uniform(-12999999, 129999999)
				stz = random.uniform(-9999999, 9999999)
			elif aot < 0.45:
				sty = random.uniform(-6300000, 6300000)
				stx = random.uniform(-6300000, 6300000)
				stz = random.uniform(-6300000, 6300000)
			else:
				sty = random.uniform(-4300000, 4300000)
				stx = random.uniform(-4300000, 4300000)
				stz = random.uniform(-4300000, 3300000)
			stssx = random.uniform(-1250, 1250)
			stssy = random.uniform(-1250, 1250)
			stssz = random.uniform(-1250, 1250)
			nst = random.uniform(0, 1)
			stsss = random.uniform(0.01, 100)
			nsttt = random.uniform(0, 1)
			sto = random.choice(["MD", "HD"])
			stnr = str(f"star-{sto}{stn}")
			#pl
			plsh = random.randint(0, 11)
			pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
			plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
			plr = random.uniform(0.01, 9000000)
			plt = random.uniform(-273.15, 1700)
			plm = random.uniform(0.01, 1100)
			plx = stx + random.uniform(-0.99, 0.99)
			ply = sty + random.uniform(-0.99, 0.99)
			plz = stz + random.uniform(-0.99, 0.99)
			plssx = stssx + random.randint(-1, 1)
			plssy = stssy + random.randint(-1, 1)
			plssz = stssz + random.randint(-1, 1)
			#black holes
			#sh
			bft = random.uniform(0, 1)
			bhn = random.choice(["Sagittarius", 			"Stranger", "Toflatos", "Taronos", "Ton"])
			bhnn = random.choice(["*", "J", "M", "L", "K", "R", "V", "C", "H"])
			cprt = random.randint(1, 2)
			bhnnn = random.randint(1, 999)
			bhsh = random.uniform(0, 1)
			#metric bh
			bhm = random.uniform(1000, 	1500000000)
			bhr = random.uniform(100000, 1000000000000)
			bhx = random.uniform(-12999999, 12999999)
			bhy = random.uniform(-10999999, 10999999)
			bhz = random.uniform(-999999, 999999)
			#speed
			bhssx = random.uniform(-3500, 3500)
			bhssy = random.uniform(-3500, 3500)
			bhssz = random.uniform(-3500, 3500)
			for gpc in range (aott):
				if aosh < 0.00007:
					zvezdscpl += 1
					aosh = random.uniform(0, 1)
					aon = random.choice(["Пелея", "Мирра", "Глаз Вселенной", "Лея", "Странник", "Коса"])
					aonk = random.choice(["X", "J","R", "F", "L", "C", "T"])
					aonkj = random.randint(1, 99)
					aoy = random.uniform(-10999999, 10999999)
					aox = random.uniform(-12999999, 129999999)
					aoz = random.uniform(-9999999, 9999999)
					aossx = random.uniform(-1250, 1250)
					aossy = random.uniform(-1250, 1250)
					aossz = random.uniform(-1250, 1250)
					ksm.write("\n\nnewsys:\n")
					ksm.write(f'''\nЗвездное скопление: {aon} {aonk} {aonkj}\n''')
					ksm.write(f'''\nкоординаты в галактике {galx}:\n''')
					ksm.write(f'''x: {aox:.2f}\ny: {aoy:.2f}\nz: {aoz:.2f}''')
					ksm.write(f'''\n\nspeed:\n\n''')
					ksm.write(f'''x: {aossx:.2f}км/с\ny: {aossy:.2f}км/с\nz: {aossz:.2f}км/с''')
					rtj = random.randint(120, 11000)
					aot = random.uniform(0, 1)
					amsh = random.randint(1, 4)
					for glcp in range (rtj):
						zvdscp += 1
						stm = random.uniform(0.01, 600)
						stl = random.uniform(100, 2500)
						stn = random.randint(100, 30000)
						stt = random.randint(1000, 42000)
						ste = random.uniform(0.01, 13.8)
						if aot < 0.30:
							sty = aoy + random.uniform(-5000, 5000)
							stx = aox + random.uniform(-5000, 5000)
							stz = aoz + random.uniform(-5000, 5000)
						elif aot < 0.45:
							sty = aoy + random.uniform(-4500, 4500)
							stx = aox + random.uniform(-4500, 4500)
							stz = aoz + random.uniform(-4500, 4500)
						else:
							sty = aoy + random.uniform(-3500, 3500)
							stx = aox + random.uniform(-3500, 3500)
							stz = aoz + random.uniform(-3500, 3500)
						stssx = aossx + random.uniform(-125, 125)
						stssy = aossy + random.uniform(-125, 125)
						stssz = aossz + random.uniform(-125, 125)
						nst = random.uniform(0, 1)
						stsss = random.uniform(0.01, 100)
						nsttt = random.uniform(0, 1)
						sto = random.choice(["MD", "HD"])
						stnr = str(f"star-{sto}{stn}")
						ksm.write("\n\nnewsys:")
						ksm.write(f'''\nв звездном скоплении: {aon} {aonk} {aonkj}''')
						if nst < 0.005:
							neutronzvezd += 1
							stsss = random.uniform(1000000, 12000000000)
							stm = random.uniform(0.1, 45)
							ste = random.uniform(0.001, 0.25)
							stt = random.uniform(0.0001, 10000000)
							ksm.write(f'''\n\nтип: нейтронная звезда''')
							if nsttt < 0.03:
								magn += 1
								ksm.write('''\n\nтип нейтронной звезды: магнетар''')
							elif nsttt < 0.4:
								kvz += 1
								ksm.write('''\n\nтип нейтронной звезды: квазар''')
							elif nsttt < 1:
								puls += 1
								ksm.write('''\n\nтип нейтронной звезды: пульсар''')
							else:
								pass
						else:
							zvezd += 1
							ksm.write(f'''\n\nтип: обычная звезда''')
						ksm.write(f'''\nstar-{sto}{stn}-galaxy-{galx}''')
						ksm.write(f'''\nmass sun-{stm:.2f}''')
						ksm.write(f'''\ntemperature-{stt:.2f}c°''')
						ksm.write(f'''\n\nlife-{ste:.3f}-billion years''')
						ksm.write(f'''\nspeed spin-{stsss:.2f}/год\n''')
						ksm.write(f'''\n\nкоординаты в галактике {galx}''')
						ksm.write(f'''\nx: {stx:.3f}-light year''')
						ksm.write(f'''\ny: {sty:.3f}-light year''')
						ksm.write(f'''\nz: {stz:.3f}-light year''')
						ksm.write(f'''\nspeed: \nx:{stssx:.2f}км/с\ny:{stssy:.2f}км/с\nz:{stssz:.2f}км/с''')
						ksm.write('''\n\nпо температуре:\n''')
						if stt < 3700:
							ksm.write('''\nэто красный карлик!''')
							ksm.write('''\nобозначение: M\n''')
						elif stt < 5200:
							ksm.write('''\nэто оранжевый карлик!''')
							ksm.write('''\nобозначение: K\n''')
						elif stt < 6000:
							ksm.write('''\nэто желтый карлик!''')
							ksm.write('''\nобозначение: G\n''')
						elif stt < 7500:
							ksm.write('''\nэто желто-белый карлик!''')
							ksm.write('''\nобозначение: F''')
						elif stt < 10000:
							ksm.write('''\nэто белый карлик!''')
							ksm.write('''\nобозначение: A\n''')
						elif stt < 30000:
							ksm.write('''\nэто бело-голубой карлик!''')
							ksm.write('''\nобозначение: B\n''')
						elif stt < 50000:
							ksm.write('''\nэто голубой карлик!''')
							ksm.write('''\nобозначение: O\n''')
						elif stt < 100000:
							ksm.write('''\nэто голубой сверхгигант!''')
							ksm.write('''\nобозначение: O+\n''')
						elif stt > 100000:
							ksm.write('''\nэто сверх монстр с абсолютной температурой!''')
							ksm.write('''\nобозначение: O++\n''')
						else:
							ksm.write('''\nпоздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
					else:
						pass
					
				
			
			for cpg in range (cprt):
				if bhsh < 0.009:
					bft = random.uniform(0, 1)
					if bft < 0.006:
						bhm = random.uniform(1000000, 	1500000000)
						bhr = random.uniform(100000, 1000000000000)
						ksm.write("\n\nnewsys:")
						blackholesv += 1
						ksm.write(f'''\n\nтип: сверхмасивная черная дыра''')
						ksm.write(f'''\nназвание: {bhn} {bhnn}  {bhnnn}''')
						ksm.write(f'''\n\nсолнечная масса: {bhm:.2f}''')
						ksm.write(f'''\nрадиус: {bhr:.2f}''')
						ksm.write(f'''\n\nкоординаты в галактике {galx}:\n''')
						ksm.write(f'''x: {bhx:.2f}\ny: {bhy:.2f}\nz: {bhz:.2f}''')
						ksm.write(f'''\n\nскорость:\n''')
						ksm.write(f'''x: {bhssx:.2f}км/с\ny: {bhssy:.2f}км/с\nz: {bhssz:.2f}км/с''')
						bhnnn = random.randint(1, 999)
						bhsh = random.uniform(0, 1)
						bhm = random.uniform(1000, 	1500000)
						bhr = random.uniform(100000, 10000000000)
						bhx = random.uniform(-12999999, 12999999)
						bhy = random.uniform(-10999999, 10999999)
						bhz = random.uniform(-999999, 999999)
						bhssx = random.uniform(-3500, 3500)
						bhssy = random.uniform(-3500, 3500)
						bhssz = random.uniform(-3500, 3500)
						bhn = random.choice(["Sagittarius", 			"Stranger", "Toflatos", "Taronos", "Ton"])
						bhnn = random.choice(["*", "J", "M", "L"])
					else:
						ksm.write("\n\nnewsys:")
						blackhole += 1
						ksm.write(f'''\n\nтип: черная дыра\n''')
						ksm.write(f'''\nназвание: {bhn} {bhnn}  {bhnnn}''')
						ksm.write(f'''\n\nсолнечная масса: {bhm:.2f}''')
						ksm.write(f'''\nрадиус: {bhr:.2f}''')
						ksm.write(f'''\n\nкоординаты в галактике {galx}:\n''')
						ksm.write(f'''x: {bhx:.2f}\ny: {bhy:.2f}\nz: {bhz:.2f}''')
						ksm.write(f'''\n\nскорость:\n''')
						ksm.write(f'''x: {bhssx:.2f}\ny: {bhssy:.2f}\nz: {bhssz:.2f}''')
						bhnnn = random.randint(1, 999)
						bhsh = random.uniform(0, 1)
						bhm = random.uniform(1000, 	1500000)
						bhr = random.uniform(100000, 10000000000)
						bhx = random.uniform(-12999999, 12999999)
						bhy = random.uniform(-10999999, 10999999)
						bhz = random.uniform(-999999, 999999)
						bhssx = random.uniform(-3500, 3500)
						bhssy = random.uniform(-3500, 3500)
						bhssz = random.uniform(-3500, 3500)
						bhn = random.choice(["Sagittarius", 			"Stranger", "Toflatos", "Taronos", "Ton"])
						bhnn = random.choice(["*", "J", "M", "L"])
				else:
					pass
				

			#ast
			ash = random.uniform(0, 1)
			am = random.uniform(0.0001, 3)
			an = random.choice(["Kenos", "Jebos", "Masos", "Rafus", "Egas", "Vatos", "Karas"])
			ann = random.choice(["GJ", "GF", "GM"])
			annn = random.choice(["I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX", "X"])
			ar = random.uniform(0.1, 1000)
			ax = stx + random.uniform(-0.99, 0.99)
			ay = sty + random.uniform(-0.99, 0.99)
			az = stz + random.uniform(-0.99, 0.99)

			assx = stssx + random.randint(-1, 1)
			assy = stssy + random.randint(-1, 1)
			assz = stssz + random.randint(-1, 1)
			asss = random.uniform(0.01, 50)
			if nst < 0.005:
				neutronzvezd += 1
				stsss = random.uniform(10000000, 12000000000)
				stm = random.uniform(0.1, 45)
				ste = random.uniform(0.001, 0.25)
				stt = random.uniform(0.0001, 10000000)
				ksm.write("\n\nnewsys:")
				ksm.write(f'''\n\nтип: нейтронная звезда''')
				plsh = 0
				if nsttt < 0.03:
					magn += 1
					ksm.write('''\n\nтип нейтронной звезды: магнетар''')
				elif nsttt < 0.4:
					kvz += 1
					ksm.write('''\n\nтип нейтронной звезды: квазар''')
				elif nsttt < 1:
					puls += 1
					ksm.write('''\n\nтип нейтронной звезды: пульсар''')
				else:
					pass
			else:
				zvezd += 1
				ksm.write("\n\nnewsys:")
				ksm.write(f'''\n\nтип: обычная звезда''')
                
			ksm.write(f'''\nstar-{sto}{stn}-galaxy-{galx}''')
			ksm.write(f'''\nmass sun-{stm:.2f}''')
			ksm.write(f'''\ntemperature-{stt:.2f}c°''')
			ksm.write(f'''\n\nlife-{ste:.3f}-billion years''')
			ksm.write(f'''\nspeed spin-{stsss:.2f}/год\n''')
			ksm.write(f'''\n\nкоординаты в галактике {galx}''')
			ksm.write(f'''\nx: {stx:.3f}-light year''')
			ksm.write(f'''\ny: {sty:.3f}-light year''')
			ksm.write(f'''\nz: {stz:.3f}-light year''')
			ksm.write(f'''\nspeed: \nx:{stssx:.2f}км/с\ny:{stssy:.2f}км/с\nz:{stssz:.2f}км/с''')
			ksm.write('''\n\nпо температуре:\n''')
			if stt < 3700:
				ksm.write('''\nэто красный карлик!''')
				ksm.write('''\nобозначение: M\n''')
			elif stt < 5200:
				ksm.write('''\nэто оранжевый карлик!''')
				ksm.write('''\nобозначение: K\n''')
			elif stt < 6000:
				ksm.write('''\nэто желтый карлик!''')
				ksm.write('''\nобозначение: G\n''')
			elif stt < 7500:
				ksm.write('''\nэто желто-белый карлик!''')
				ksm.write('''\nобозначение: F''')
			elif stt < 10000:
				ksm.write('''\nэто белый карлик!''')
				ksm.write('''\nобозначение: A\n''')
			elif stt < 30000:
				ksm.write('''\nэто бело-голубой карлик!''')
				ksm.write('''\nобозначение: B\n''')
			elif stt < 50000:
				ksm.write('''\nэто голубой карлик!''')
				ksm.write('''\nобозначение: O\n''')
			elif stt < 100000:
				ksm.write('''\nэто голубой сверхгигант!''')
				ksm.write('''\nобозначение: O+\n''')
			elif stt > 100000:
				ksm.write('''\nэто сверх монстр с абсолютной температурой!''')
				ksm.write('''\nобозначение: O++\n''')
			else:
				ksm.write('''\nпоздравляю! вы открыли новую звезду которую еще никогда не находили!:D''')
			for pl in range (plsh):
				planets += 1
				ksm.write(f'''\n\nplanet name: {pln} {plnn}''')
				ksm.write(f'''\nearth mass: {plm:.3f}''')
				ksm.write(f'''\nradius: {plr:.2f}км''')
				ksm.write(f'''\ngalaxy: {galx}''')
				ksm.write(f'''\nin system: {stnr}''')
				ksm.write(f'''\ntemperature: {plt:.2f}c°''')
				ksm.write('''\n\nкоординаты планеты:\n''')
				ksm.write(f'''\nx: {plx:.3f}''')
				ksm.write(f'''\ny: {ply:.3f}''')
				ksm.write(f'''\nz: {plz:.3f}''')
				ksm.write(f'''\n\nскорость:''')
				ksm.write(f'''\nx: {plssx:.2f}км/с''')
				ksm.write(f'''\ny: {plssy:.2f}км/с''')
				ksm.write(f'''\nz: {plssz:.2f}км/с\n\n''')
				plsh = random.randint(0, 11)
				pln = random.choice(["Charlie", "Gilbert", "Egrinch", "Etarius", "Ratus", "Manches", "Ompus", "Olimpus", "Kertys", "Tynys", "Mechas", "Lampos", "Karatus", "Kenos", "Rembatros", "Nekas"])
				plnn = random.choice(["I","II","III","IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"])
				plr = random.uniform(0.01, 9000000)
				plt = random.uniform(-273.15, 1700)
				plm = random.uniform(0.01, 1100)
				plx = stx + random.uniform(-0.99, 0.99)
				ply = sty + random.uniform(-0.99, 0.99)
				plz = stz + random.uniform(-0.99, 0.99)
				plssx = stssx + random.randint(-1, 1)
				plssy = stssy + random.randint(-1, 1)
				plssz = stssz + random.randint(-1, 1)
				if ash < 0.15:
					for et in range (amsh):
						asteroids += 1
						ksm.write(f'''\n\nподраздел: {ann}''')
						ksm.write(f'''\nasteroid: {an} {annn}''')
						ksm.write(f'''\nmass: {am:.2f}''')
						ksm.write(f'''\nin system: {stnr}''')
						ksm.write(f'''\nin galaxy: {galx}''')
						ksm.write(f'''\n\nкоординаты:\n''')
						ksm.write(f'''\nx: {ax:.2f}''')
						ksm.write(f'''\ny: {ay:.2f}''')
						ksm.write(f'''\nz: {az:.2f}''')
						ksm.write('''\n\nскорость:\n''')
						ksm.write(f'''\nx: {assx:.2f}км/с''')
						ksm.write(f'''\ny: {assy:.2f}км/с''')
						ksm.write(f'''\nz: {assz:.2f}км/с\n''')
						ksm.write(f'''\nspins: {asss:.2f}/year''')
						ash = random.uniform(0, 1)
						am = random.uniform(0.0001, 3)
						an = random.choice(["Kenos", "Jebos", "Masos", "Rafus", "Egas", "Vatos", "Karas"])
						ann = random.choice(["GJ", "GF", "GM"])
						annn = random.choice(["I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX", "X"])
						ar = random.uniform(0.1, 1000)
						ax = stx + random.uniform(-0.99, 0.99)
						ay = sty + random.uniform(-0.99, 0.99)
						az = stz + random.uniform(-0.99, 0.99)

						assx = stssx + random.randint(-1, 1)
						assy = stssy + random.randint(-1, 1)
				else:
					ash = random.uniform(0, 1)
		blacabs = blackhole + blackholesv
		with open(
		f"stats-{galx}.txt", "a"
		)  as sts:
			sts.write(f'''KNGG stats generator''')
			sts.write(f"\n\nseed 1 = {seedf}")
			sts.write(f"\nseed 2 = {seedt}")
			sts.write(f'''\n\ngalaxy: {galx}\n''')
			sts.write(f'''\nвсего звезд: {zvezd}''')
			sts.write(f'''\nнейтронных звезд: {neutronzvezd}\nтипы нейтронных звезд:\nпульсаров: {puls}\nквазаров: {kvz}\nмагнетаров: {magn}\n\n''')
			sts.write(f'''черных дыр: {blacabs}\nсверхмассивных черных дыр: {blackholesv}\nобычных черных дыр: {blackhole}\n\n''')
			sts.write(f'''астероидов: {asteroids}\n\n''')
			sts.write(f'''планет: {planets}\n\n''')
			sts.write(f'''звездных скоплений: {zvezdscpl}\nзвезд в звездных скоплениях: {zvdscp}''')
		with open(f"stats-{galx}.txt", "r") as jkl:
		    stsrd = jkl.read()
		    qr = qrcode.make(stsrd)
		    qr.save(f"qrcode-{galx}.jpg")
		os.makedirs("galaxy_photos", exist_ok=True)
		os.makedirs("galxphto", exist_ok=True)
		os.chdir("galxphto")
		bimg = Image.open("blank.jpg")
		hjj = 255, 255, 255, 255
		try:
			fnt = ImageFont.truetype("arial.ttf", 70)
			mfnt = ImageFont.truetype("arial.ttf", 44)
		except:
			fnt = ImageFont.truetype("/system/fonts/DroidSans.ttf", 70)
			mfnt = ImageFont.truetype("/system/fonts/DroidSans.ttf", 44)
		drw = ImageDraw.Draw(bimg)
		glxtp = random.choice(["Эллиптическая", "Спиральная", "Линзовидная"])
		if glxtp == "Эллиптическая":
			gimg = random.choice(["elip1.jpg", "elip2.jpg"])
		elif glxtp == "Спиральная":
			gimg = random.choice(["spir1.jpg", "spir2.jpg"])
		else:
			gimg = random.choice(["linz1.jpg", "linz2.jpg"])
		fgimg = Image.open(gimg)
		drw.text((300, 15), f'''галактика {galx}''', font=fnt, fill=hjj)
		drw.text((324, 80), f'''тип галактики {glxtp}''', font=mfnt, fill=hjj)
		drw.text((80, 160), f'''звезд {zvezd}''', font=mfnt, fill=hjj)
		drw.text((80, 210), f'''нейтронных звезд {neutronzvezd}''', font=mfnt, fill=hjj)
		drw.text((80, 260), f'''звездныхскоплений {zvezdscpl}''', font=mfnt, fill=hjj)
		drw.text((80, 310), f'''черных дыр {blacabs}''', font=mfnt, fill=hjj)
		drw.text((80, 360), f'''планет {planets}''', font=mfnt, fill=hjj)
		drw.text((80, 410), f'''астероидов {asteroids}''', font=mfnt, fill=hjj)
		sz = (890, 760)
		rfgimg = fgimg.resize(sz)
		bimg.paste(rfgimg, (160, 520))
		bimg.save(f"{galx}.jpg")
		os.rename(f"{galx}.jpg", f"{oldir}/galaxies/galaxy_photos/{galx}.jpg")
		zvdscp = 0
		zvezd = 0
		neutronzvezd = 0
		planets = 0
		asteroids = 0
		blackholesv = 0
		blackhole = 0
		zvezdscpl = 0
		kvz = 0
		puls = 0
		magn = 0
		
def mein():
	print("KNGGS Generator")
	print("BY NYA18")
	print("""0.- выход\n1.- воспроизвести сид""")
	try:
		inpt = int(input(":  "))
	except:
		print("\nвведи число!!:)\n")
		mein()
	if inpt == 0:
		print("bye bye:>")
	elif inpt == 1:
		print("введи 1 сид")
		try:
			inpf = int(input(":  "))
			if inpf > 999999 or inpf < 100000:
				print("""1 сид может быть только в диапазоне 100000-999999""")
				mein()
			else:
				pass
		except:
			print("\nвведи число!!:)\n")
			mein()
		print("введи 2 сид")
		try:
			inpg = int(input(":  "))
		except:
			print("\nвведи число!!:)\n")
			mein()
		galaxies(inpf, inpg)
		mein()
	else:
		print("""\nвведи правильный выбор ;}\n""")
		mein()
mein()