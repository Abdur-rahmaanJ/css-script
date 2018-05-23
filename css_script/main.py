# -*- coding: utf-8 -*-
"""
            CSS SCRIPT 
"""

from collections import OrderedDict
import random
import math
 
class CssScript:
    def __init__(self, source):
        #
        #   HTML TEMPLATES PARTS
        #
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
        self.output = open('C:/Users/Dell/Desktop/entry/git/css-script-candy/css_script/output.html', 'w+')
        
        #
        #   SHAPE GLOBAL PROPERTIES
        #
        self.bg_col = 'black'
        self.rotation = 0
        self.translation = 0
        
        self.X = ''
        self.Y = ''
        
        #
        #   REGISTRIES
        #
        self.funcs = {0:1}
        self.vars = {0:1}
        self.colors = {}
        
        self.source = open(source, 'r')
        
        #
        #   FLAGS
        #
        self.funcpass = False
        self.looppass = False
        
        #
        #   ONGOING DATA
        #
        self.ongoing_func = ''
        self.ongoing_loop_times = ''
        
        #
        #   ONGOING BODIES
        #
        self.glass = ''
        self.loopbody = ''
        
        #
        #   COUNTS
        #
        self.line = 1
        
    #
    #   OUTPUT
    #
        
    def out(self, x):
        self.output.write(x)
        
    #
    #   BASE ELEMENT
    #
    def elem(self, x, y, styles, classes='', content=''):
        return '    <div style="position:absolute;left:{}px;top:{}px;transform:rotate({}deg);\
{}" class=" {}">{}</div>\n'.format(x, y, self.rotation, styles, classes, content)

    #
    #   DERIVED ELEMENTS
    #
    
    #
    # BASICS
    #

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
                
    #
    # SPECIFIC SHAPES - ARROWS
    #
                
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
    #
    # SPECIFIC SHAPES - OTHERS
    #
                
    #
    #   TEXT
    #
    
    def text(self, x, y, text):
        self.out(
                self.elem(x, y, 'color:{};'.format(self.bg_col), content=text)
            )
        
    # 
    #   GLOBAL PROPERTIES
    #
                
    def fill(self, x):
        self.bg_col = x
        
    def rotate(self, x):
        self.rotation = x
        
    #
    #   RESOLVE DIGIT VALUE
    #
    def resolve_digit(self, registry, value):
        '''
        checks if value is digit or if variable, fetches it's value
        else returns none
        '''
        if value.isdigit():
            return value
        elif '|' in value:
            wds  = value.split('|')
            if wds[0] == 'rand' and len(wds) == 3:
                l = int(self.resolve_digit(registry, wds[1]))
                h = int(self.resolve_digit(registry, wds[2]))
                return random.randint(l, h)
            elif wds[0] == 'sine' and len(wds) == 2:
                val = int(self.resolve_digit(registry, wds[1]))
                return math.sin(val)
            elif wds[0] == 'cos' and len(wds) == 2:
                val = int(self.resolve_digit(registry, wds[1]))
                return math.cos(val)
            elif wds[0] == 'abssine' and len(wds) == 2:
                val = int(self.resolve_digit(registry, wds[1]))
                return abs(math.sin(val))      
        else:
            try:
                return registry[value]
            except KeyError:
                return None
    
    def resolve_col(self, registry, value):
        if '|' in value:
            wds  = list(filter((lambda x:x!=''), value.split('|')))
            if wds[0] == 'randCol' and len(wds) == 1:
                return 'rgb({},{},{})'.format(random.randint(0,255),
                            random.randint(0,255), random.randint(0,255)
                            )
        else:
            return value
        
    #
    #   INDEPENDENT KEYWORD PARSE
    #
    def parse(self, registry, command, params):
        # TODO : add registry parameter to use in both local and func context
        params = params.strip()
        if command == 'circle':
            params = params.split(' ')
            if len(params) == 4:
                x = self.resolve_digit(registry, params[0])
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                self.circle(x, y, sizex, sizey)
                
        elif command == 'rect':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 4:
                x = self.resolve_digit(registry, params[0]) 
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                self.rect(x, y, sizex, sizey)
                
        elif command == 'roundRect':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 8:
                x = self.resolve_digit(registry, params[0]) 
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                br = self.resolve_digit(registry, params[4])
                bl = self.resolve_digit(registry, params[5])
                tr = self.resolve_digit(registry, params[6])
                tl = self.resolve_digit(registry, params[7])
                self.roundRect(x, y, sizex, sizey,  br, bl, tr, tl)
                
        elif command == 'arrowUp':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 4:
                x = self.resolve_digit(registry, params[0]) 
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                self.arrowUp(x, y, sizex, sizey)
        elif command == 'arrowDown':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 4:
                x = self.resolve_digit(registry, params[0]) 
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                self.arrowDown(x, y, sizex, sizey)
        elif command == 'arrowRight':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 4:
                x = self.resolve_digit(registry, params[0]) 
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                self.arrowRight(x, y, sizex, sizey)
        elif command == 'arrowLeft':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 4:
                x = self.resolve_digit(registry, params[0]) 
                y = self.resolve_digit(registry, params[1])
                sizex = self.resolve_digit(registry, params[2])
                sizey = self.resolve_digit(registry, params[3])
                self.arrowLeft(x, y, sizex, sizey)
                
        elif command == 'fill':
            color = self.resolve_col(registry, params)
            self.fill(color)
            
        elif command == 'rotate':
            self.rotate(self.resolve_digit(registry, params))
            
        elif command == 'text':
            params = params.split(' ')
            x = self.resolve_digit(registry, params[0])
            y = self.resolve_digit(registry, params[1])
            self.text(x, y, ' '.join(params[2:]))
            
        #
        #   VAL MODIFS
        #
        elif command == 'set':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            if len(params) == 2 and params[0].isdigit() == False:
                var_value = self.resolve_digit(registry, params[1]) 
                var_name = params[0]
                self.vars[var_name] = var_value
                # print(self.vars)
            else:
                print('wrong assignment format')
        # TODO : ADD COLOUR VARS
                
        elif command == 'do':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            op = params[0]
            val = self.resolve_digit(registry, params[1])
            var = params[3]
            if params[2] == 'to':
                if op == '+':
                    registry[var] = float(registry[var]) + float(val)
                if op == '-':
                    registry[var] = float(registry[var]) - float(val)
                if op == '*':
                    registry[var] = float(registry[var]) * float(val)
                if op == '/':
                    registry[var] = float(registry[var]) // float(val)
        
        #
        #   DENUG / SHOW
        #
        elif  command == 'show':
            params = list(filter((lambda x:x!=''), params.split(' ')))
            try:
                x = self.resolve_digit(registry, params[0])
                y = self.resolve_digit(registry, params[1])
                self.text(x, y, registry[params[2]])
            except KeyError:
                print('key undefined')
                
    #
    #   NON-WORD KEYWORD PARSE AND FLAGS
    #
    def passover(self, source):
        for l in source.readlines():
            # print(self.vars)
            if self.funcpass == True: # before to not include + line
                self.glass += l
            if self.looppass == True: # before to not include + line
                self.loopbody += l
                
            if l == '\n':
                if self.funcpass == True:
                    self.funcs[self.ongoing_func]['body'] = self.glass
                    # self.funcs[---] = {'params':{}, 'body':{}}
                    self.glass = ''
                    self.funcpass = False
                    self.ongoing_func = ''
                    print(self.glass)
                if self.looppass == True:
                    for i in range(int(self.ongoing_loop_times)):
                        for line in self.loopbody.strip('\n').split('\n'):
                            x = line.strip('\n').split(' ', 1)
                            self.parse( self.vars, x[0], x[1])
                    self.ongoing_loop_times = ''
                    self.looppass = False
                    self.loopbody = ''
                continue
            
            elif l[0] == '#':
                continue
            elif l[0] == '+':
                wds = l.strip('\n').split(' ')
                self.funcpass = True
                fname = wds[1].strip()
                self.ongoing_func = fname
                if len(wds) == 2:
                    self.funcs[fname] = {'params':None, 'body':''}
                    # print(fname.replace('\n','#'))
                elif len(wds) > 2:
                    param_names = wds[2:]
                    params = OrderedDict()
                    for p in param_names:
                        params[p] = None
                    self.funcs[fname] = {'params':params, 'body':''}
                    
            elif l.split(' ', 1)[0] == 'call':
                # TODO add resolve-digits to parameters of funcs
                wds = l.strip('\n').split(' ')
                fname = wds[1]
                # TODO : ADD A READ STR FUNC INSTEAD OF READLINE
                try:
                    if self.funcs[fname]['params'] == None:
                        for line in self.funcs[fname]['body'].strip('\n').split('\n'):
                            x = line.strip('\n').split(' ', 1)
                            self.parse( self.vars, x[0], x[1])
                    else: # TODO resolve digit for parameters
                        params = wds[2:]
                        i = 0
                        for key in self.funcs[fname]['params']:
                            self.funcs[fname]['params'][key] = params[i]
                            i += 1
                        for line in self.funcs[fname]['body'].strip('\n').split('\n'):
                            x = line.strip('\n').split(' ', 1)
                            self.parse( self.funcs[fname]['params'], x[0], x[1])
                except KeyError:
                    print('no such func exists')
                    
            elif l[:4] == 'loop':
                wds = l.strip('\n').split(' ')
                self.looppass = True
                self.ongoing_loop_times = wds[1]
            if self.funcpass == False:
                line = l.strip('\n').split(' ', 1)
                command = line[0]
                params = line[1]
                self.parse(self.vars, command, params)        
    
    #
    #   ABSTRACTED METHODS
    #         
    def init(self):
        self.output.write(self.header)
        print('begun')
        
    def end(self):
        self.output.write(self.footer)
        self.output.flush()
        self.output.close()
        print('ended')
        
    #
    #   CALLABLE METHOD
    #
    def exec(self):
        self.init()
        self.passover(self.source)
        self.end()

if __name__ == '__main__':
    script = CssScript('C:/Users/Dell/Desktop/entry/git/css-script-candy/css_script/file.candy')
    script.exec()
    









