class Mesh:
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    def get_vertices(self):
        return self.vertices

    def get_faces(self):
        return self.faces
