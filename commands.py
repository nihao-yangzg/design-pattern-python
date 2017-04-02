#coding=utf-8
###------------------------------------------###
###                命令模式                   ###
###------------------------------------------###
from copy import deepcopy

class Fan(object):
    HIGH = 3
    MEDIA = 2
    LOW = 1
    STOP = 0
    OFF = 'OFF'
    ON = 'ON'
    def __init__(self):
        self.speed = self.STOP
        self.status = self.OFF


    def off(self):
        self.status = self.OFF
        self.speed = self.STOP

    def on(self):
        self.status = self.ON
        self.speed = self.LOW

    def low(self):
        self.status = self.ON

    def media(self):
        self.speed = self.MEDIA

    def high(self):
        self.speed = self.HIGH 

    def copy(self, fan):
        self.speed = fan.speed
        self.status = fan.status

    def __str__(self):
        return 'speed: ' + str(self.speed) + '\n' \
               'switch: ' + self.status

class Command(object):
    def __init__(self):
        raise SyntaxError('can not initialize')

    def execute(self):
        raise SyntaxError('has not overrided')

    def undo(self):
        raise SyntaxError('has not overrided')

class MediaControlCommand(Command):
    def __init__(self, fan):
        self.fan = fan
    def execute(self):
        self.undo_fan = deepcopy(self.fan)
        print self.undo_fan
        self.fan.media()

    def undo(self):
        self.fan.copy(self.undo_fan)
        


class HighControlCommand(Command):
    def __init__(self, fan):
        self.fan = fan
    def execute(self):
        self.undo_fan = deepcopy(self.fan)
        self.fan.high()

    def undo(self):
        self.fan.copy(self.undo_fan)


class LowControlCommand(Command):
    def __init__(self, fan):
        self.fan = fan
    def execute(self):
        self.undo_fan = deepcopy(self.fan)
        self.low()

    def undo(self):
        self.fan.copy(self.undo_fan)


class OffControlCommand(Command):
    def __init__(self, fan):
        self.fan = fan
    def execute(self):
        self.undo_fan = deepcopy(self.fan)
        self.fan.off()

    def undo(self):
        pass



class OnControlCommand(Command):
    def __init__(self, fan):
        self.fan = fan
    def execute(self):
        self.undo_fan = deepcopy(self.fan)
        self.fan.on()

    def undo(self):
        pass


class NoCommand(object):
    def execute(self):
        pass


class ControlPanel(object):
    def __init__(self, fan):
        self.fan = fan
        self.commands = dict()
        for item in ['on', 'off', 'low', 'media', 'high']:
            self.commands[item] = NoCommand()
        self.executors = list()

    def set_command(self, command, name):
        self.commands[name] = command(self.fan)
    def onHighButtonPushed(self):
        self.executors.append('high')
        self.commands['high'].execute()
    def onMediaButtonPushed(self):
        self.executors.append('media')
        self.commands['media'].execute()
    def onLowButtonPushed(self):
        self.executors.append('low')
        self.commands['low'].execute()
    def onOffButtonPushed(self):
        self.executors.append('off')
        self.commands['off'].execute()
    def onOnButtonPushed(self):
        self.executors.append('on')
        self.commands['on'].execute()
    def onUndoPushed(self):
        name = self.executors.pop()
        print name
        self.commands[name].undo()

if __name__ == '__main__':
    fan = Fan()
    controlpanel = ControlPanel(fan)
    
    controlpanel.set_command(LowControlCommand, 'low')
    controlpanel.set_command(HighControlCommand, 'high')
    controlpanel.set_command(MediaControlCommand, 'media')

    controlpanel.set_command(OnControlCommand, 'on')
    controlpanel.set_command(OffControlCommand, 'off')

    print fan
    controlpanel.onOnButtonPushed()
    controlpanel.onMediaButtonPushed()
    controlpanel.onHighButtonPushed()
    print fan
    controlpanel.onUndoPushed()
    print fan
    controlpanel.onUndoPushed()
    print fan
