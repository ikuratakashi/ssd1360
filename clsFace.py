from clsLineData import clsLineData
class clsFace:
    def Normal(self) -> list[clsLineData] :

        result = []
        result.append([39,9,39,23,1])
        result.append([87,9,87,23,1])
        result.append([53,45,63,51,1])
        result.append([73,45,63,51,1])

        return result
    
    def NormalEyeClose(self) -> list[clsLineData] :

        result = []
        result.append([34,16,44,16,1])
        result.append([82,16,92,16,1])
        result.append([53,45,63,51,1])
        result.append([73,45,63,51,1])

        return result