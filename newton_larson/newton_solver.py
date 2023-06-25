from sympy import *
import numpy as np
import io
import base64
import matplotlib
matplotlib.use('SVG')
import matplotlib.pyplot as plt
init_printing(use_unicode=True)

class newton_rapson:
    
    iteration_list = list()
    x_n = None
    have_sol = True
    
    def __init__(self,function__, x_0, error__) -> None:
        self.x_0 = x_0
        self.x = symbols('x')
        self.error_ = error__
        #Conversion de funcion str a funcion operable
        self.function_ = sympify(function__)
        self.derivated_function = diff(self.function_, self.x)
        self.iterable_ecuation = self.function_ / self.derivated_function
        try:
            g2 = int(self.iterable_ecuation.evalf(subs = {self.x : self.x_0}))
        except:
            self.have_sol = False
            
        #Todo listo!! ahora a iterar y almacenar en la lista de diccio
    
    def __del__(self):
            self.iteration_list = list()
            self.x_n = None
            self.have_sol = True
            
    def iterate(self):
        if(self.have_sol):
            #iteraciones a partir de atributos de la clase
            try:
                exit_ = True
                valor_x = None
                self.x_n = self.x_0
                counter = 0
                error_ = 100.0
                bad_initial = 0
                x_zero_negative = False
                x_zero_positive = False
                x_r_n = False
                x_r_p = False
                while(exit_):
                    #if(self.derivated_function.evalf(subs = {self.x : self.x_0})):
                       # self.have_sol = False
                       # return self.have_sol
                    counter += 1
                    valor_x = self.x_n
                    denom_ = (self.derivated_function.evalf(subs = {self.x : self.x_n})) 
                    if(x_zero_positive == False and denom_ == 0):
                        x_zero_positive = True
                        self.x_n += 0.0000001
                    if(x_zero_positive == True and x_zero_negative == False and denom_ == 0):
                        x_zero_negative = True
                        self.x_n -= 0.0000001
                    if(denom_ == 0 and x_zero_negative == True and x_zero_positive == True):
                        actual_iterate = np.array([counter, valor_x, 0, 0])
                        self.iteration_list.append(actual_iterate)
                        return True
                    self.x_n = round(valor_x - (self.iterable_ecuation.evalf(subs = {self.x : valor_x})), 10)
                    #zero?
                    if(x_r_n == True and x_r_p == True):
                        actual_iterate = np.array([counter, valor_x, 0, 0])
                        self.iteration_list.append(actual_iterate)
                        return True
                    if(self.x_n == 0 and valor_x > 0):
                        self.x_n -= 0.0000001
                        x_r_p = True
                    if(self.x_n == 0 and valor_x < 0):
                        self.x_n += 0.0000001
                        x_r_n = True
                    try:
                        temp__ = error_
                        error_ = (100 * (self.x_n - valor_x) / self.x_n)
                        if(error_ == nan):
                            return False
                        
                        if(error_ <= 0):
                            error_ *= -1
                        actual_iterate = np.array([counter, valor_x, self.x_n, error_])
                    except:
                        print('')
                    
                    self.iteration_list.append(actual_iterate)
                    if error_ <= self.error_:
                        exit_ = False
                    if(error_ > temp__ ):
                        bad_initial += 1
                    if(bad_initial == 100):
                        dt = 'S'
                        if(dt == "N" or dt == "n"):
                            print('lejano')
                            self.have_sol = False
                            exit_ = False
                    if(counter > 100000):
                        print("El problema no tiene solucion cercana al valor de x")
                        self.have_sol = False
                        exit_ = False
            except ValueError as vl:
                print("El dato de entrada parece no estar comprendido dentro de la funcion" + vl)   
                self.have_sol = False      
        else:
            print("La ecuacion no tiene solucion ya que no esta en funcion\n" +
                  "de una sola variable o intenta iterar raiz en un numero negativo")
        return self.have_sol
        
    def return_data(self):
        return self.iteration_list
    """ 
    def steep_by(self):
        print("La funcion a iterar es:")
        pprint(self.function_)
        print("Y la derivada de la funcion: ")
        pprint(self.derivated_function)
        input()
        print("Una vez tenemos la funcion derivada procedemos\n" +
              "a dividir la ecuacion por su forma derivada..\n\n" +
              "Al simplificar obtenemos:")
        pprint(self.iterable_ecuation)
        input()
        print("Ahora que tenemos la funcion necesaria solo\n" +
              "resta empezar a  iterar reemplazando el valor" +
              "inicial " + str(self.x_0) +" en la funcion")
        temp_ = (self.iterable_ecuation.evalf(subs = {self.x : self.x_0}))
        print("Asi obteniendo: " + str(temp_))
        input()
        print("Para obtener el valor del nuevo x debemos tomar" +
              "el antiguo valor de x y restarle el valor obtenido:")
        print("Antiguo x : " + str(self.x_0) + " - Valor de F(x) : " + str(temp_) + "" +
              "Resultado del nuevo valor de x :" + str(self.x_0 - temp_) + "\n")
        input()
        print("Una vez hecho esto solo nos queda encontrar " +
              "el margen de error... Para ello tendremos que restar el" +
              "antiguo x al nuevo x y dividir entre el nuevo valor de x")
        input()
        print("En este caso el porcentaje de error es de " + str(self.iteration_list[0][3]) + "%")
        input()
        print("Listo!! ahora solo queda repetir el proceso hasta que" +
              "se llegue al margen de error deseado!")
        input()
    """
    #imprimir imagenes
    
    #grafica de margen de error
    def generate_graphic_error(self):
        fig, ax = plt.subplots()
        iteration_number = list()
        iteration_error = list()
        datas_ = np.array(self.iteration_list)
        for item_ in datas_:
            iteration_number.append(item_[0])
            iteration_error.append(item_[3])
        iteration_number = np.array(iteration_number)
        iteration_error = np.array(iteration_error)
        #define the error graphic
        ax.plot(iteration_number, iteration_error, color = 'tab:green', marker = 'o')
        ax.set_title('Grafica de valores de margen de error %', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
        #se genera el archivo
        buf_ = io.BytesIO()
        plt.savefig(buf_, format='png')
        buf_.seek(0)
        image64_error = base64.b64encode(buf_.getvalue()).decode()
        return image64_error

    #grafica de funcion ingresada
    def generate_graphic_function(self):
        fig, ax = plt.subplots()
        
        function_y = list()
        datas_ = np.array(self.iteration_list)
        solution_branch = datas_[len(datas_)-1][1]
        solution_branch = int(solution_branch)
        
        x_value_list = range(solution_branch-7, solution_branch+7)
        for x_val in x_value_list:
            cx = self.function_.evalf(subs = {self.x : x_val})
            function_y.append(cx)
        x_zeros = [0] * len(x_value_list)
        y_zeros = [0] * len(function_y)
        x_value_list = np.array(x_value_list)
        function_y = np.array(function_y)
        #define the x graphic
        ax.plot(x_value_list, function_y, color = 'tab:red')
        ax.plot(x_value_list, x_zeros, color='tab:blue')
        ax.plot(y_zeros, function_y, color='tab:blue')
        solution_branch = datas_[len(datas_)-1][1]
        ax.plot(solution_branch, 0,marker="o", color="red")
        branch_tag = 0
        if(function_y[0] < function_y[len(function_y)-1]):
            branch_tag = (function_y[len(function_y)-1] - function_y[1]) * 0.08
        else:
            branch_tag = (function_y[1] - function_y[len(function_y)-1]) * 0.1
        plt.text(solution_branch - 0.5, branch_tag, 'Raiz', color = "green")
        ax.set_title('Grafica de la función', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        #se genera el archivo
        buf_ = io.BytesIO()
        plt.savefig(buf_, format='png')
        buf_.seek(0)
        image64_x = base64.b64encode(buf_.getvalue()).decode()
        return image64_x