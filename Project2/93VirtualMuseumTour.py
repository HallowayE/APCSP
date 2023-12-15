#Virtual Museum Tour: Explore museum artifacts and information virtually.

#https://stackoverflow.com/questions/35286540/how-to-display-an-image

from PIL import Image

def produceImage(i):
  img = Image.open(f'Project2/image{i}.jpg')
  img.show()
  print(info[i])

info = ["This is the ancient tablet of Arush. It's power was used to bring the sun to it's peoples' crops","This is the amulet of Kangulam. It's wearer was given the power to accelerate life and make crops grow","This is the helmet of Gongdong. It had the unique ability to controll the thought of plants. It was used to make crops grow.","This is the foutain of Jalub. It's water had a magical property that accelerated the growth of crops.","This is the scythe of Drebeign. When used to harvest a crop, it replants it and accelerates it's growth","This is the empty case of Magag. When made uneptied with a crop, it would multiply said crop","This is an old computer"]

i=0
next=""
while (next!="-1"):
  produceImage(i)
  i+=1
  next = input("press enter for next, enter -1 to escape ")
  if i>=len(info):
    i=0



#Images from SDXL Turbo