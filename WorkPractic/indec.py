from pylab import *
import numpy as np
import matplotlib.pyplot as plt
class Pais:
    provincias = [] #list para contener objetos de clase Provincia
    nombre = ""
    def __init__(self, p):
        self.provincias = p
        self.nombre = "Argentina"

    #Devuelve todos: varones + mujeres
    def get_total_poblacion(self):
        total = 0
        for p in self.provincias:
            total += p.get_total_poblacion()
        return total

    #Devuelte el objeto Provincia por el cod recibido
    def get_provincia(self, cod_provincia):
        p = None
        for x in self.provincias:
            if(x.get_cod() == cod_provincia):
                p = x
                break
        return p

    #PARA HACER :) ************************************************************
    """
        Mostrar el total de pob.
        Mostrar el total de pob. femenina
        Mostrar el total de pob. masculina
    """
    def mostrar_totales_poblacion(self):
        print('Total:',self.get_total_poblacion())
        print('    Hombres:',self.get_total_hombres())
        print('    Mujeres:',self.get_total_mujeres())
    
    def get_total_hombres(self):
        total_hombres = self.get_total_hombres_alfabetos()+self.get_total_hombres_analfabetos()
        return total_hombres
    
    def get_total_hombres_analfabetos(self):
        hombres_analfabetos = 0
        for p in self.provincias:
            hombres_analfabetos += p.alfabetismo.analfabetos.varones
        return hombres_analfabetos
    
    def get_total_hombres_alfabetos(self):
        hombres_alfabetos = 0
        for p in self.provincias:
            hombres_alfabetos += p.alfabetismo.alfabetos.varones
        return hombres_alfabetos
    
    def get_total_mujeres(self):
        total_mujeres = self.get_total_mujeres_alfabetas()+self.get_total_mujeres_analfabetas()
        return total_mujeres
    
    def get_total_mujeres_analfabetas(self):
        mujeres_analfabetas = 0
        for p in self.provincias:
            mujeres_analfabetas += p.alfabetismo.analfabetos.mujeres
        return mujeres_analfabetas
    
    def get_total_mujeres_alfabetas(self):
        mujeres_alfabetas = 0
        for p in self.provincias:
            mujeres_alfabetas += p.alfabetismo.alfabetos.mujeres
        return mujeres_alfabetas
    """
        Mostrar el nombre de provincia y su ratio de habitantes por vivienda
        Orderna por ratio descendentemente
    """
    def mostrar_ratio_habitantes_por_vivienda_por_provincia(self):
        hab_viv = []
        for p in self.provincias:
            total_viviendas = 0
            for v in p.viviendas:
                total_viviendas += v.cantidad
            percent = round(p.get_total_poblacion()/total_viviendas,2)
            name = p.nombre
            hab_viv.append((name,percent))
        for i in range(len(hab_viv)-1):
            for j in range(len(hab_viv)-i-1):
                if hab_viv[j][1] < hab_viv[j+1][1]:
                    hab_viv[j], hab_viv[j+1] = hab_viv[j+1], hab_viv[j]
        for item in hab_viv:
            print(item[0])
            print('     h/v:',item[1])
    """
        Mostrar por sexo el % de analfabetismo
    """
    def mostrar_porcentaje_analfabetismo_por_sexo(self):
        porc_h = round((self.get_total_hombres_analfabetos()*100)/self.get_total_hombres(),2)
        porc_m = round((self.get_total_mujeres_analfabetas()*100)/self.get_total_mujeres(),2)
        print('Porcentaje de analfabetismo x sexo en',self.nombre)
        print('     hombres:',porc_h,'%')
        print('     mujeres:',porc_m,'%')

    """
        Mostrar el nombre de provincia y el % de analfabetos.
        Ordenar la lista descendentemente por el %
    """
    def mostrar_porcentaje_analfabetismo_por_provincia(self):
        for p in self.provincias:
            print(p.nombre)
            h_a = p.alfabetismo.analfabetos.varones
            m_a = p.alfabetismo.analfabetos.mujeres
            total_h = p.alfabetismo.alfabetos.varones+h_a
            total_m = p.alfabetismo.alfabetos.mujeres+m_a
            print('     analfabetos:',round(((h_a+m_a)*100)/(total_h+total_m),2),'%')

    """
        Mostrar el nombre de provincia y el % de viviendas sin retrete
        Ordenar la lista descendentemente por el %
    """
    def mostrar_porcentaje_vivendas_sin_retrete_por_provincia(self):
        for p in self.provincias:
            print(p.nombre)
            cant_v = 0
            for v in p.viviendas:
                cant_v += v.cantidad
            print('     sin sanitario:',round((p.sanitario.sin_retrete*100)/cant_v,2),'%')
    """
        Mostrar el nombre de provincia y el % de los que no viven en una casa o departamento.
        Ordenar la lista descendentemente por el %
    """
    def mostrar_porcentaje_vivienda_precaria_por_provincia(self):
        for p in self.provincias:
            print(p.nombre)
            cant_v = 0
            for v in p.viviendas:
                if v.tipo != 0 and v.tipo != 3:
                    cant_v += v.cantidad
            total_v = 0
            for v in p.viviendas:
                total_v += v.cantidad
            print('     situacion precaria:',round((cant_v*100)/total_v,2),'%')

    """
        Se quiere saber si hay una correlacion entre las variables: analfabetismos vs
        viviendas precarias y sin retrete. Por ello hacer:
        1) Ordenar la lista de provincias segun el % de analfabetismos de forma
        ascendente. Esto nos da una pendiente positiva.
        2) Calcular la pendiente de la regresion lineal para las variables 
        "viviendas precarias" y para "sin retetre" y compare:
        ¿Como es el signo de la pendiente de estas dos variables comparado con
        el signo de la pendientes del % de alfabetismo?
        ¿Que se puede concluir?
    """

    def mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete(self):
        alfabetismo = []
        for p in self.provincias:
            name = p.nombre
            alfa = round((p.alfabetismo.analfabetos.get_total()*100)/p.get_total_poblacion(),2)
            cant_v = 0
            for v in p.viviendas:
                if v.tipo != 0 and v.tipo != 3:
                    cant_v += v.cantidad
            precarie = round((cant_v*100)/p.get_total_poblacion(),2)
            cant_v = 0
            for v in p.viviendas:
                cant_v += v.cantidad
            retrete = round((p.sanitario.sin_retrete*100)/cant_v,2)
            alfabetismo.append((name,alfa,precarie,retrete))
        for i in range(len(alfabetismo)-1):
            for j in range(len(alfabetismo)-i-1):
                if alfabetismo[j][1] > alfabetismo[j+1][1]:
                    alfabetismo[j], alfabetismo[j+1] = alfabetismo[j+1], alfabetismo[j]
        x = []
        y1 = []
        y2 = []
        for item in alfabetismo:
            x.append(item[1])
            y1.append(item[2])
            y2.append(item[3])
        
        n = len(x)
        x = np.array(x)
        y1 = np.array(y1)
        y2 = np.array(y2)
        sumx = sum(x)
        sumy1 = sum(y1)
        sumy2 = sum(y2)
        sumx2 = sum(x*x)
        sumxy1 = sum(x*y1)
        sumxy2 = sum(x*y2)
        promX = sumx/n
        promY1 = sumy1/n
        promY2 = sumy2/n

        m1 = (sumx*sumy1 - n*sumxy1)/(sumx**2 - n*sumx2)
        m2 = (sumx*sumy2 - n*sumxy2)/(sumx**2 - n*sumx2)
        b1 = promY1 - m1*promX
        b2 = promY2 - m2*promX

        # lo siguiente lo comente pq no se pa que es 
        # no entiendo nada de estadistica 

        # sumy12 = sum(y1*y1)
        # sumy22 = sum(y2*y2)
        # sigmax = np.sqrt(sumx2/n - promX**2)
        # sigmay1 = np.sqrt(sumy12/n - promY1**2)
        # sigmay2 = np.sqrt(sumy22/n - promY2**2)
        # sigmaxy1 = sumxy1/n - promX*promY1
        # sigmaxy2 = sumxy2/n - promX*promY2
        # R21 = (sigmaxy1/(sigmax*sigmay1))**2
        # R22 = (sigmaxy2/(sigmax*sigmay2))**2

        # print(R21)
        # print(R22)

        plt.plot(x,y1,'o',label = 'vivienda precaria')
        plt.plot(x,y2,'o',label = 'sin retrete')
        plt.plot(x,m1*x+b1,label = 'Ajuste vivienda precaria')
        plt.plot(x,m2*x+b2,label = 'Ajuste sin retrete')
        plt.xlabel('porcentaje de analfabetismo')
        plt.ylabel('porcentaje vivienda precaria y sin retrete')
        plt.title("regresion lineal")  
        plt.grid()
        plt.legend()
        plt.show()

class Provincia:
    cod = None
    nombre = None
    alfabetismo = None #para contener un objeto de la clase Alfabetismo
    sanitario = None #para contener un objeto de la clase Sanitario
    viviendas = [] #list para contener todos los tipos de viviendas
    def __init__(self, c, n, a, r, v):
        self.cod = c
        self.nombre = n
        self.alfabetismo = a
        self.sanitario = r
        self.viviendas = v

    #Devuelve todos: varones más mujeres
    def get_total_poblacion(self):
        return self.alfabetismo.get_total()
        
    def get_cod(self):
        return self.cod


class PorSexo:
    varones = None
    mujeres = None
    def __init__(self, v, m):
        self.varones = v
        self.mujeres = m
   
    #Devuelve todos: varones más mujeres
    def get_total(self):
        return self.varones + self.mujeres


class Alfabetismo:
    alfabetos = None #para contener un objeto de clase PorSexo con datos de la personas alfabetas
    analfabetos = None #para contener un objeto de clase PorSexo con datos de la personas analfabetas    
    def __init__(self, a, no_a):
        self.alfabetos = a
        self.analfabetos = no_a

    #Total de la población: alfabetas + analfabetas
    def get_total(self):
        return self.alfabetos.get_total() + self.analfabetos.get_total()


class Sanitario:
    con_retrete = None
    sin_retrete = None
    def __init__(self, c, s):
        self.con_retrete = c
        self.sin_retrete = s


class Vivienda:
    """
     TIPO (según INDEC):
        0: Casa
        1: Rancho
        2: Casilla
        3: Departamento
        4: Pieza/s en inquilinato
        5: Pieza/s en hotel o pensión
        6: Local no construido para habitación
        7: Vivienda móbil
    """
    tipo = None
    cantidad = None
    def __init__(self, t, c):
        self.tipo = t
        self.cantidad = c


#Fuente de datos: https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-135

arg = Pais([
    Provincia(0, 'Ciudad Autónoma de Buenos Aires', Alfabetismo(PorSexo(1160483, 1395255), PorSexo(5344, 7059)), Sanitario(1061211, 21787), [Vivienda(0, 252771), Vivienda(1, 565), Vivienda(2, 1884), Vivienda(3, 788791), Vivienda(4, 19571), Vivienda(5, 17082), Vivienda(6, 2237), Vivienda(7, 97)]),
    Provincia(1, '24 partidos del Gran Buenos Aires', Alfabetismo(PorSexo(3917957, 4223950), PorSexo(55416, 61809)), Sanitario(2294650, 358638), [Vivienda(0, 2212645), Vivienda(1, 17794), Vivienda(2, 73827), Vivienda(3, 329731), Vivienda(4, 12452), Vivienda(5, 1405), Vivienda(6, 5091), Vivienda(7, 343)]),
    Provincia(2, 'Interior de la provincia de Buenos Aires', Alfabetismo(PorSexo(2285525, 2438254), PorSexo(33289, 28494)), Sanitario(1625106, 146799), [Vivienda(0, 1502191), Vivienda(1, 12283), Vivienda(2, 35724), Vivienda(3, 212714), Vivienda(4, 4117), Vivienda(5, 817), Vivienda(6, 3026), Vivienda(7, 1033)]),
    Provincia(3, 'Catamarca', Alfabetismo(PorSexo(144528, 148625), PorSexo(3108, 2928)), Sanitario(75871, 13505), [Vivienda(0, 83578), Vivienda(1, 2134), Vivienda(2, 400), Vivienda(3, 2666), Vivienda(4, 427), Vivienda(5, 30), Vivienda(6, 96), Vivienda(7, 45)]),
    Provincia(4, 'Chaco', Alfabetismo(PorSexo(394795, 411225), PorSexo(22440, 24292)), Sanitario(916669, 61884), [Vivienda(0, 236946), Vivienda(1, 12558), Vivienda(2, 5696), Vivienda(3, 12052), Vivienda(4, 2048), Vivienda(5, 165), Vivienda(6, 424), Vivienda(7, 244)]),
    Provincia(5, 'Chubut', Alfabetismo(PorSexo(205779, 206044), PorSexo(4049, 4265)), Sanitario(197102, 51742), [Vivienda(0, 122955), Vivienda(1, 1479), Vivienda(2, 1917), Vivienda(3, 19318), Vivienda(4, 1068), Vivienda(5, 58), Vivienda(6, 237), Vivienda(7, 144)]),
    Provincia(6, 'Córdoba', Alfabetismo(PorSexo(1314229, 1425717), PorSexo(22334, 18451)), Sanitario(176147, 93986), [Vivienda(0, 840488), Vivienda(1, 5929), Vivienda(2, 2775), Vivienda(3, 124044), Vivienda(4, 2852), Vivienda(5, 791), Vivienda(6, 1199), Vivienda(7, 475)]),
    Provincia(7, 'Corrientes', Alfabetismo(PorSexo(372493, 399455), PorSexo(17969, 16523)), Sanitario(136043, 11133), [Vivienda(0, 210288), Vivienda(1, 13056), Vivienda(2, 8147), Vivienda(3, 14201), Vivienda(4, 2293), Vivienda(5, 236), Vivienda(6, 393), Vivienda(7, 230)]),
    Provincia(8, 'Entre Ríos', Alfabetismo(PorSexo(486281, 519080), PorSexo(12294, 9610)), Sanitario(326978, 30272), [Vivienda(0, 317956), Vivienda(1, 3805), Vivienda(2, 7273), Vivienda(3, 26680), Vivienda(4, 644), Vivienda(5, 176), Vivienda(6, 495), Vivienda(7, 221)]),
    Provincia(9, 'Formosa', Alfabetismo(PorSexo(200956, 206992), PorSexo(7821, 9575)), Sanitario(79122, 51012), [Vivienda(0, 109807), Vivienda(1, 12203), Vivienda(2, 1514), Vivienda(3, 4124), Vivienda(4, 2104), Vivienda(5, 44), Vivienda(6, 229), Vivienda(7, 109)]),
    Provincia(10, 'Jujuy', Alfabetismo(PorSexo(261419, 269965), PorSexo(5404, 11784)), Sanitario(122201, 32710), [Vivienda(0, 134293), Vivienda(1, 7286), Vivienda(2, 2595), Vivienda(3, 7824), Vivienda(4, 2510), Vivienda(5, 74), Vivienda(6, 245), Vivienda(7, 84)]),
    Provincia(11, 'La Pampa', Alfabetismo(PorSexo(128679, 133208), PorSexo(2805, 2227)), Sanitario(101706, 3091), [Vivienda(0, 95356), Vivienda(1, 458), Vivienda(2, 169), Vivienda(3, 8239), Vivienda(4, 317), Vivienda(5, 10), Vivienda(6, 177), Vivienda(7, 71)]),
    Provincia(12, 'La Rioja', Alfabetismo(PorSexo(131833, 136616), PorSexo(2843, 2154)), Sanitario(75564, 10803), [Vivienda(0, 77743), Vivienda(1, 1970), Vivienda(2, 1643), Vivienda(3, 4208), Vivienda(4, 597), Vivienda(5, 56), Vivienda(6, 105), Vivienda(7, 45)]),
    Provincia(13, 'Mendoza', Alfabetismo(PorSexo(681053, 730907), PorSexo(15527, 16003)), Sanitario(421292, 38258), [Vivienda(0, 398510), Vivienda(1, 7618), Vivienda(2, 1985), Vivienda(3, 48846), Vivienda(4, 1686), Vivienda(5, 216), Vivienda(6, 595), Vivienda(7, 94)]),
    Provincia(14, 'Misiones', Alfabetismo(PorSexo(412901, 422882), PorSexo(17110, 18662)), Sanitario(201604, 88659), [Vivienda(0, 249745), Vivienda(1, 7866), Vivienda(2, 11548), Vivienda(3, 16938), Vivienda(4, 3376), Vivienda(5, 77), Vivienda(6, 560), Vivienda(7, 153)]),
    Provincia(15, 'Neuquén', Alfabetismo(PorSexo(219539, 225070), PorSexo(5120, 5339)), Sanitario(145697, 13605), [Vivienda(0, 130466), Vivienda(1, 1924), Vivienda(2, 3425), Vivienda(3, 21312), Vivienda(4, 1743), Vivienda(5, 83), Vivienda(6, 228), Vivienda(7, 121)]),
    Provincia(16, 'Río Negro', Alfabetismo(PorSexo(255390, 262917), PorSexo(6541, 6539)), Sanitario(171370, 19227), [Vivienda(0, 155561), Vivienda(1, 2149), Vivienda(2, 4091), Vivienda(3, 27071), Vivienda(4, 1230), Vivienda(5, 72), Vivienda(6, 331), Vivienda(7, 92)]),
    Provincia(17, 'Salta', Alfabetismo(PorSexo(459258, 478751), PorSexo(12710, 17657)), Sanitario(202113, 64962), [Vivienda(0, 220293), Vivienda(1, 14806), Vivienda(2, 11076), Vivienda(3, 17161), Vivienda(4, 2881), Vivienda(5, 120), Vivienda(6, 450), Vivienda(7, 288)]),
    Provincia(18, 'San Juan', Alfabetismo(PorSexo(260076, 278149), PorSexo(6360, 5133)), Sanitario(142970, 19234), [Vivienda(0, 134753), Vivienda(1, 11219), Vivienda(2, 1075), Vivienda(3, 14489), Vivienda(4, 405), Vivienda(5, 43), Vivienda(6, 196), Vivienda(7, 24)]),
    Provincia(19, 'San Luis', Alfabetismo(PorSexo(170030, 177358), PorSexo(3674, 2838)), Sanitario(108089, 9677), [Vivienda(0, 104692), Vivienda(1, 1125), Vivienda(2, 470), Vivienda(3, 10380), Vivienda(4, 654), Vivienda(5, 106), Vivienda(6, 208), Vivienda(7, 131)]),
    Provincia(20, 'Santa Cruz', Alfabetismo(PorSexo(113297, 106023), PorSexo(1291, 1213)), Sanitario(72841, 3392), [Vivienda(0, 64118), Vivienda(1, 524), Vivienda(2, 852), Vivienda(3, 9339), Vivienda(4, 1181), Vivienda(5, 43), Vivienda(6, 118), Vivienda(7, 58)]),
    Provincia(21, 'Santa Fe', Alfabetismo(PorSexo(1273525, 1383361), PorSexo(25003, 23092)), Sanitario(862253, 86116), [Vivienda(0, 793209), Vivienda(1, 10303), Vivienda(2, 8279), Vivienda(3, 132409), Vivienda(4, 2023), Vivienda(5, 796), Vivienda(6, 1119), Vivienda(7, 231)]),
    Provincia(22, 'Santiago del Estero', Alfabetismo(PorSexo(328348, 340598), PorSexo(14809, 13061)), Sanitario(122529, 75377), [Vivienda(0, 169162), Vivienda(1, 20833), Vivienda(2, 1097), Vivienda(3, 5830), Vivienda(4, 463), Vivienda(5, 75), Vivienda(6, 223), Vivienda(7, 223)]),
    Provincia(23, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur', Alfabetismo(PorSexo(52991, 50430), PorSexo(347, 358)), Sanitario(35041, 1648), [Vivienda(0, 25108), Vivienda(1, 102), Vivienda(2, 3817), Vivienda(3, 7326), Vivienda(4, 226), Vivienda(5, 43), Vivienda(6, 44), Vivienda(7, 23)]),
    Provincia(24, 'Tucumán', Alfabetismo(PorSexo(557210, 596990), PorSexo(15859, 13295)), Sanitario(276897, 58924), [Vivienda(0, 287900), Vivienda(1, 4931), Vivienda(2, 11031), Vivienda(3, 30431), Vivienda(4, 897), Vivienda(5, 184), Vivienda(6, 344), Vivienda(7, 103)])
])

print("")
print('poblacion x provincia:',arg.get_provincia(0).get_total_poblacion())
print("")
print('poblacion total:',arg.get_total_poblacion())
print("\nTotales de poblacion:")
arg.mostrar_totales_poblacion() # listo
print("")
arg.mostrar_ratio_habitantes_por_vivienda_por_provincia() # listo
print("")
arg.mostrar_porcentaje_analfabetismo_por_sexo() # listo
print("")
arg.mostrar_porcentaje_analfabetismo_por_provincia() #listo
print("")
arg.mostrar_porcentaje_vivendas_sin_retrete_por_provincia() # listo
print("")
arg.mostrar_porcentaje_vivienda_precaria_por_provincia() # listo
print("")
arg.mostrar_correlacion_alfabetismo_vs_vivienda_y_retrete() # listo

print("\n")

