#!/usr/bin/python
# -*- coding: utf-8 -*-

from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    Vec3,
    Point3,
    DirectionalLight,
    PointLight,
    Spotlight,
    PerspectiveLens,
    VBase4,
    AmbientLight,)
from direct.actor.Actor import Actor

__author__ = "Fireclaw the Fox"
__license__ = """
Simplified BSD (BSD 2-Clause) License.
See License.txt or http://opensource.org/licenses/BSD-2-Clause for more info
"""


class Main(ShowBase):
    def __init__(self):
        """initialise and start the Game"""
        ShowBase.__init__(self)

        self.accept("escape", exit)
        render.setShaderAuto(True)

        #
        # SIMPLE LEVEL SETUP
        #
        self.ralph = Actor("Ralph",
                           {"idle": "Ralph-Idle",
                            "walk": "Ralph-Walk",
                            "run": "Ralph-Run"})
        self.ralph.loop("idle")
        self.ralph.reparentTo(render)
        self.ralph.setPos(0, 3, -2)
        #self.ralph.setScale(10)
        self.ralphIval = self.ralph.hprInterval(5.0, Vec3(-360, 0, 0))
        self.ralphIval.loop()
        #self.ralph.setH(-20)

        self.environment = loader.loadModel("environment")
        self.environment.reparentTo(render)
        self.environment.setScale(0.08)
        self.environment.setPos(-0.5, 15, -2)

        base.trackball.node().setHpr(0, 22, 0)

        #
        # Lights
        #
        alight = AmbientLight("Ambient")
        alight.setColor(VBase4(0.3, 0.3, 0.3, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)

        slight = Spotlight("slight")
        slight.setColor(VBase4(1, 1, 1, 1))
        # Use a 512x512 resolution shadow map
        slight.setShadowCaster(True, 2048, 2048)
        lens = PerspectiveLens()
        lens.setFov(45)
        slight.setLens(lens)
        slnp = render.attachNewNode(slight)
        slnp.setPos(5, -10, 5)
        slnp.lookAt(0, 3, -2)
        render.setLight(slnp)

        #sun = DirectionalLight("Sun")
        #sun.setColor(VBase4(1.0, 1.0, 0.9, 1))
        #sunnp = render.attachNewNode(sun)
        #sunnp.setHpr(10, -60, 0)
        #render.setLight(sunnp)

APP = Main()
APP.run()
