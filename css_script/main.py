# -*- coding: utf-8 -*-
"""
            CSS SCRIPT 
"""
 
class CssScript:
    def __init__(self, source):
        self.header = """
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <style type="">
    </style>
</head>
<body>
<div style="position:relative;">
        """
        self.footer = """
</div>
</body>
</html>
        """
        # TODO : add paramters to funcs verify '3'.isdigit()
        self.output = open('output.html', 'w+')
        self.bg_col = 'black'
        self.X = ''
        self.Y = ''
        
        self.funcs = {0:1}
        self.vars = {0:1}
        
        self.source = open(source, 'r')
        
        self.funcpass = False
        self.glass = ''
        self.ongoing_func = ''
        
        self.line = 1
        
    def out(self, x):
        self.output.write(x)

    def elem(self, x, y, styles, classes='', content=''):
        return '    <div style="position:absolute;left:{}px;top:{}px;{}" class=" {}">{}</div>\n'.format(x, 
                                    y, styles, classes, content)

    def circle(self, x, y, width, height):
        self.out(
                self.elem(x, y, 'width:{}px;height:{}px;background-color:{};border-radius:50%;'.format(width, 
                height, self.bg_col))
            )
                
    def rect(self, x, y, width, height):
        self.out(
                self.elem(x, y, 'width:{}px;height:{}px;background-color:{};'.format(width, 
                height, self.bg_col))
            )
    def roundRect(self, x, y, width, height, br, bl, tr, tl):
        self.out(
                self.elem(x, y, 'width:{}px;height:{}px;background-color:{};\
border-bottom-right-radius:{}px;border-bottom-left-radius:{}px;\
border-top-right-radius:{}px;border-top-left-radius:{}px;\
                '.format(width, 
                height, self.bg_col, br, bl, tr, tl))
            )
                
    def arrowUp(self, x, y, width, height):
        self.out(
                self.elem(x, y, 'width: 0;height: 0;border-left: {}px solid \
transparent;border-right: {}px solid transparent;border-bottom: {}px \
solid {};'.format(int(width)/2, int(width)/2,height, self.bg_col))
            )
                
    def arrowDown(self, x, y, width, height):
        self.out(
                self.elem(x, y, 'width: 0;height: 0;border-left: {}px solid \
transparent;border-right: {}px solid transparent;border-top: {}px \
solid {};'.format(int(width)/2, int(width)/2,height, self.bg_col))
            )
    
    def arrowRight(self, x, y, width, height):
        self.out(
                self.elem(x, y, 'width: 0;height: 0;border-top: {}px solid \
transparent;border-bottom: {}px solid transparent;border-left: {}px \
solid {};'.format(int(width)/2, int(width)/2,height, self.bg_col))
            )
                
    def arrowLeft(self, x, y, width, height):
        self.out(
                self.elem(x, y, 'width: 0;height: 0;border-top: {}px solid \
transparent;border-bottom: {}px solid transparent;border-right: {}px \
solid {};'.format(int(width)/2, int(width)/2,height, self.bg_col))
            )
                
    def text(self, x, y, text):
        self.out(
                self.elem(x, y, 'color:{};'.format(self.bg_col), content=text)
            )
                
    def fill(self, x):
        self.bg_col = x
        
    def resolve_digit(self, registry, value):
        '''
        checks if value is digit or if variable, fetches it's value
        else returns none
        '''
        if value.isdigit():
            return value
        else:
            try:
                return registry[value]
            except KeyError:
                return None
        
    def parse(self, command, params):
        # TODO : add registry parameter to use in both local and func context
        if command == 'circle':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(self.vars, params[0])
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                self.circle(x, y, sizex, sizey)
                
        elif command == 'rect':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(self.vars, params[0]) 
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                self.rect(x, y, sizex, sizey)
                
        elif command == 'roundRect':
            params = params.split(' ')
            if len(params) == 8:
                x = self.resolve_digit(self.vars, params[0]) 
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                br = self.resolve_digit(self.vars, params[4])
                bl = self.resolve_digit(self.vars, params[5])
                tr = self.resolve_digit(self.vars, params[6])
                tl = self.resolve_digit(self.vars, params[7])
                self.roundRect(x, y, sizex, sizey,  br, bl, tr, tl)
                
        elif command == 'arrowUp':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(self.vars, params[0]) 
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                self.arrowUp(x, y, sizex, sizey)
        elif command == 'arrowDown':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(self.vars, params[0]) 
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                self.arrowDown(x, y, sizex, sizey)
        elif command == 'arrowRight':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(self.vars, params[0]) 
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                self.arrowRight(x, y, sizex, sizey)
        elif command == 'arrowLeft':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(self.vars, params[0]) 
                y = self.resolve_digit(self.vars, params[1])
                sizex = self.resolve_digit(self.vars, params[2])
                sizey = self.resolve_digit(self.vars, params[3])
                self.arrowLeft(x, y, sizex, sizey)
                
        elif command == 'fill':
            self.fill(params)
            
        elif command == 'text':
            params = params.split(' ')
            x = self.resolve_digit(self.vars, params[0])
            y = self.resolve_digit(self.vars, params[1])
            self.text(x, y, ' '.join(params[2:]))
            
        elif command == 'set':
            params = params.split(' ')
            if len(params) == 2 and params[0].isdigit() == False:
                var_value = self.resolve_digit(self.vars, params[1]) 
                var_name = params[0]
                self.vars[var_name] = var_value
                # print(self.vars)
            else:
                print('wrong assignment format')
             
    def passover(self, source):
        for l in source.readlines():
            #print(self.funcs)
            if self.funcpass == True: # before to not include + line
                self.glass += l
                
            if l == '\n':
                if self.funcpass == True:
                    self.funcs[self.ongoing_func]['body'] = self.glass
                    # self.funcs[---] = {'params':{}, 'body':{}}
                    self.glass = ''
                    self.funcpass = False
                    self.ongoing_func = ''
                    print(self.glass)
                continue
            elif l[0] == '#':
                continue
            elif l[0] == '+':
                self.funcpass = True
                fname = l.strip('\n').split(' ', 1)[1].strip()
                self.funcs[fname] = {'params':{}, 'body':''}
                self.ongoing_func = fname
                print(fname.replace('\n','#'))
            elif l.split(' ', 1)[0] == 'call':
                fname = l.strip('\n').split(' ', 1)[1].strip()
                # TODO : ADD A READ STR FUNC INSTEAD OF READLINE
                try:
                    for line in self.funcs[fname]['body'].strip('\n').split('\n'):
                        x = line.strip('\n').split(' ', 1)
                        self.parse(x[0], x[1])
                except KeyError:
                    print('no such func exists')
            if self.funcpass == False:
                line = l.strip('\n').split(' ', 1)
                command = line[0]
                params = line[1]
                self.parse(command, params)        
             
    def init(self):
        self.output.write(self.header)
        print('begun')
        
    def end(self):
        self.output.write(self.footer)
        self.output.flush()
        self.output.close()
        print('ended')
        
    def exec(self):
        self.init()
        self.passover(self.source)
        self.end()

   
#def style(type, content):
#    return '{type_}\n{{  {content_}}}'.format(type_=type, content_=content)

script = CssScript('file.candy')
script.exec()
    









