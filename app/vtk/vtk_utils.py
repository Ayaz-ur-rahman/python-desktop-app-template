def create_sphere():
    # Utility function to create a VTK sphere
    sphere = vtk.vtkSphereSource()
    sphere_mapper = vtk.vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere.GetOutputPort())
    sphere_actor = vtk.vtkActor()
    sphere_actor.SetMapper(sphere_mapper)
    return sphere_actor
