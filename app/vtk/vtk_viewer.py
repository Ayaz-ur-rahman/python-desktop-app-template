from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtkmodules.all as vtk

class VTKViewer(QVTKRenderWindowInteractor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.renderer = vtk.vtkRenderer()
        self.GetRenderWindow().AddRenderer(self.renderer)
        self.interactor = self.GetRenderWindow().GetInteractor()
        self.initialize_scene()

    def initialize_scene(self):
        sphere = vtk.vtkSphereSource()
        sphere_mapper = vtk.vtkPolyDataMapper()
        sphere_mapper.SetInputConnection(sphere.GetOutputPort())
        sphere_actor = vtk.vtkActor()
        sphere_actor.SetMapper(sphere_mapper)
        self.renderer.AddActor(sphere_actor)
        self.renderer.SetBackground(0.1, 0.2, 0.4)
        self.GetRenderWindow().Render()
