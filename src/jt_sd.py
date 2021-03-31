######
# JT Class for each key
#
#
#

import requests as r

class jtSD():
    
    def __init__(self):
        self.kState = {}
        for x in range(33):
            self.kState[x] = False
        self.kStr = {0:'Play',
						1:'Pause',
						2:'VolUp',
						3:'VolDown',
						4:'Next',
						5:'Previous',
						6:'',
						7:'',
						8:'Study On',
						9:'Study On',
						10:'',
						11:'',
						12:'',
						13:'',
						14:'',
						15:'',
						16:'',
						17:'',
						18:'',
						19:'',
						20:'',
						21:'',
						22:'',
						23:'',
						24:'UC On',
						25:'UC Off',
						26:'',
						27:'',
						28:'',
						29:'',
						30:'',
						31:'',
						32:'',
					}
        self.kIcon ={0:'play',
                        1:'pause',
                        2:'volUp',
                        3:'volDown',
                        4:'next',
                        5:'prev',
                        6:'',
                        7:'',
                        8:'lightsOn',
                        9:'lightsOff',
                        10:'',
                        11:'',
                        12:'',
                        13:'',
                        14:'',
                        15:'',
                        16:'',
                        17:'',
                        18:'',
                        19:'',
                        20:'',
                        21:'',
                        22:'',
                        23:'',
                        24:'lightsOn',
                        25:'lightsOff',
                        26:'',
                        27:'',
                        28:'',
                        29:'',
                        30:'',
                        31:'',
                        32:''
                      }
        return
    
    def pressKey(self,keyID):
        eStr = 'self.k' + str(keyID) + '()'
        eval(eStr)
        print(self.kState[int(keyID)])
        
    def k0(self):
        #r.get('http://127.0.0.1:5000/study?play')
        r.get('http://192.168.1.10:1880/sd/sonos/play')
        print('k0')
    
    def k1(self):
        #r.get('http://127.0.0.1:5000/study?pause')
        r.get('http://192.168.1.10:1880/sd/sonos/pause')
        print('k1')
    
    def k2(self):
        r.get('http://192.168.1.10:1880/sd/sonos/vup')
        print('k2')
    
    def k3(self):
        r.get('http://192.168.1.10:1880/sd/sonos/vdwn')
        print('k3')
    
    def k4(self):
        r.get('http://192.168.1.10:1880/sd/sonos/next')
        print('k4')
    
    def k5(self):
        r.get('http://192.168.1.10:1880/sd/sonos/previous')
        print('k5')
    
    def k6(self):
        print('k6')
    
    def k7(self):
        print('k7')
    
    def k8(self):
        r.get('http://192.168.1.10:1880/sd/hue/study/on')
        print('k_8')
    
    def k9(self):
        r.get('http://192.168.1.10:1880/sd/hue/study/off')
        print('k_9')
    
    def k10(self):
        print('k10')
    
    def k11(self):
        print('k11')
    
    def k12(self):
        print('k12')
    
    def k13(self):
        print('k13')
    
    def k14(self):
        print('k14')
    
    def k15(self):
        print('k15')
    
    def k16(self):
        print('k16')
    
    def k17(self):
        print('k17')
    
    def k18(self):
        print('k18')
    
    def k19(self):
        print('k19')
    
    def k20(self):
        print('k20')
    
    def k21(self):
        print('k21')
    
    def k22(self):
        print('k22')
    
    def k23(self):
        print('k23')
    
    def k24(self):
        r.get('http://192.168.1.10:1880/sd/hue/utility/on')
        print('k24')
    
    def k25(self):
        r.get('http://192.168.1.10:1880/sd/hue/utility/off')
        print('k25')
    
    def k26(self):
        print('k26')
    
    def k27(self):
        print('k27')
    
    def k28(self):
        print('k28')
    
    def k29(self):
        print('k29')
    
    def k30(self):
        print('k30')
    
    def k31(self):
        print('k31')
    
    def k32(self):
        print('k32')

















