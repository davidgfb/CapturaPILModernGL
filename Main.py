from moderngl_window import WindowConfig, run_window_config
from moderngl_window.geometry import quad_fs

from PIL.ImageGrab import grab

class App(WindowConfig):
    window_size = 900, 600
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.quad, self.program = quad_fs(),\
                                self.ctx.program(vertex_shader =\
        '''#version 460
        in vec3 in_position; //vertices pantalla

        void main() {
            gl_Position = vec4(in_position, 1); //rasteriza pantalla en fragmentos, vertices --> fragmentos
        }''', fragment_shader =\
        '''#version 460
        uniform sampler2D tex;

        out vec4 fragColor; //color para cada fragmento

        void main() {        
            fragColor = texture(tex, gl_FragCoord.xy/vec2(900,-600));
        }''') 
        
    def render(self, time, frame_time):
        img = grab()
        tex = self.ctx.texture(img.size, 3, img.tobytes(), alignment=4)
        tex.use() 
        
        self.ctx.clear()       
        self.quad.render(self.program) #uniform tiene q estar inicializado en glsl


run_window_config(App)




        
