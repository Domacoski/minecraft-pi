from mcpi.minecraft import Minecraft

x, y, z = mc.player.getPos()



mc.postToChat("POSICAO")

mc.postToChat(str( mc.getPos() ))


mc.player.setPos(x, y+100, z)
mc.postToChat("Y ")

