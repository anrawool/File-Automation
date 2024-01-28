import pyscreenshot
pic = pyscreenshot.grab(bbox=(150, 150, 1600, 1600))
pic.show()
pic.save("ss.png")
