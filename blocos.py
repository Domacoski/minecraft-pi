from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()



mc.postToChat("BLOCOS...")

x, y, z = mc.player.getPos()
mc.postToChat("SET BLOCK")
mc.setBlock(x+1, y, z, 1)
mc.postToChat("SET NETHER_REACTOR")
mc.setBlock(x+3, y, z, block.NETHER_REACTOR_CORE.id)
