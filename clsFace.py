from clsLineData import clsLineData
class clsFace:
    def Normal(self) -> list[clsLineData] :
        '''通常の顔'''

        result = []

        # 目
        result.append([39,9,39,23,1])
        result.append([87,9,87,23,1])
        
        # 口
        result.append([53,45,63,51,1])
        result.append([73,45,63,51,1])

        return result
    
    def NormalEye(self) -> list[clsLineData] :
        '''通常の顔 目のみ'''

        result = []

        # 目
        result.append([39,9,39,23,1])
        result.append([87,9,87,23,1])
        
        # 口
        #result.append([53,45,63,51,1])
        #result.append([73,45,63,51,1])

        return result
    
    def NormalEyeClose(self) -> list[clsLineData] :
        '''通常の顔 目を閉じる'''

        result = []

        # 目
        result.append([34,16,44,16,1])
        result.append([82,16,92,16,1])
        
        # 口
        #result.append([53,45,63,51,1])
        #result.append([73,45,63,51,1])

        return result
    
    def Wow(self) -> list[clsLineData] :
        '''驚いた顔'''

        result = []

        # 目
        result.append([39,9,39,23,1])
        result.append([87,9,87,23,1])
        
        # 口
        result.append([63,35,58,48,1])
        result.append([63,35,68,48,1])
        result.append([58,48,63,51,1])
        result.append([68,48,63,51,1])

        return result
    
    def WowEx(self) -> list[clsLineData] :
        '''すごく驚いた顔'''

        result = []

        # 目
        result.append([40,10,48,16,1])
        result.append([40,22,48,16,1])
        result.append([86,10,78,16,1])
        result.append([86,22,78,16,1])
        
        # 口
        result.append([63,35,58,48,1])
        result.append([63,35,68,48,1])
        result.append([58,48,63,51,1])
        result.append([68,48,63,51,1])

        return result