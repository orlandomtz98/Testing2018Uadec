import unittest
from unittest.mock import Mock
from dos_youtube import AppYoutube
from main import *
from Youtube import Video, AbstractRepo, AbstractYoutube
from base_de_datos import SQlite

class TestYTapp(unittest.TestCase):

    def setUp(self):

        self.yt = AppYoutube()
        self.videomock = Mock(ID="5", Titulo = "Dimitri Vegas & Like Mike - Melody à Tomorrowland 2015", Duracion = "PT2M12S", NombreCanal = "Antoine Cardon",  Fecha= "2016-05-21T22:54:45.000Z", Likes = self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Likes, Vistas = self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Vistas, Descripcion = "Melody, le dernier son de Dimitri Vegas & Like Mike, à tomorrowland 2015 en Belgique .",Compartidas="150")
        self.video = Video(self.videomock.Titulo,self.videomock.Duracion,self.videomock.NombreCanal,self.videomock.Fecha,self.videomock.Likes,self.videomock.Vistas,self.videomock.Descripcion)
        #self.sql = GuardarVideo()
        #self.sql.GuardarVideo(self.video)
        print(self.videomock)

        ################################
        self.video2 = Video("videochido",12,"CanalChido", "26 nov 2018", '2500', '10000',"video")
        self.video2.Id=1
        self.video2.Compartidas=100
    #Hace las pruebas de guardar un video y que todos sus atributos estén almacenados correctamente
    def test_Video(self):

        print("test_Video")
        self.assertEqual(self.video2.Id, 1)
        self.assertEqual(self.video2.Titulo, "videochido")
        self.assertEqual(self.video2.Duracion, 12 )
        self.assertEqual(self.video2.NombreCanal, "CanalChido")
        self.assertEqual(self.video2.Fecha, "26 nov 2018" )
        self.assertEqual(self.video2.Likes, "2500")
        self.assertEqual(self.video2.Vistas, "10000")
        self.assertEqual(self.video2.Descripcion, "video")
        print("Terminado")



#    def test_modVideo(self):

#        print("test_modVideo")
#        SQlite.ModificarVideo(self.video2.Id,self.video2.Compartidas)
#        actual=SQlite.MostrarVideo(self.video2.Id)
#        expected=[self.video2.Id,'video1',12,'El video', "12 nov 2018", 2500, 10000,'video',self.video2.Compartidas]
#        self.assertListEqual(expected,actual)

    def test_borrar(self):

        print("test_borrar")
        SQlite.BorrarVideo(self.video2.Id)
        actual=SQlite.MostrarVideo(self.video2.Id)
        expected=[]
        self.assertListEqual(expected,actual)
        print("Terminado prueba borrar")

    def mostrar_video(self):
        print("Test_Mostrar")
        x=SQlite.MostrarVideo(self.video2.Id)
        expected=['video1','12','El video', "12 nov 2018", '2500', '10000','video']
        self.assertListEqual(expected,x)
        print("Terminado prueba mostrar")

    


    def test_infoVideo(self):

        print("test_infoVideo")
        #self.assertEqual((5), self.video.ID)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Titulo, self.video.Titulo)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Duracion, self.video.Duracion)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").NombreCanal, self.video.NombreCanal)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Fecha, self.video.Fecha)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Likes, self.video.Likes)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Vistas, self.video.Vistas)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=IEI9MDjDiao").Descripcion, self.video.Descripcion)
        print("Terminado prueba info video")


if __name__ == '__main__':
    unittest.main()
