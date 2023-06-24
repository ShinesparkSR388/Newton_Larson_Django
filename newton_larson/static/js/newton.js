function keyb_(){
    //crear elementos
        //PRINCIPALES
        const container = document.querySelector('[form-problem]');
        const in_problem = document.getElementById('id_problem');
        const in_x = document.getElementById('id_x');
        const in_error = document.getElementById('id_error');
        const label_problem = document.createElement('h3');
        const label_x = document.createElement('h3');
        const label_error = document.createElement('h3');
        const btn_sub = document.querySelector('[btn_sub]')
        //TECLADO
        const button_per_file = 6
        const container_keyboard = document.createElement('div');
        container_keyboard.classList.add('padding-2','margin-left-3','margin-right-3', 'border');
        const value_entry = ['+','-','*','/','(',')','x','(x**2)','sqrt(','sin(','cos()','tan()'];
        const value_show = ['+','-','×','/','(',')','(x)','x²','√','sin','cos','tan()'];
        let var_ = 0;
        let div_row;
        value_entry.forEach(element => {
            if(var_ % button_per_file == 0){
                div_row = document.createElement('div');
                div_row.classList.add('row','flex-container', 'flex-justify-left');
                container_keyboard.appendChild(div_row);
            }
            const btn_n = document.createElement('div');
            btn_n.classList.add('margin-0','margin-bottom-1','bg-color-2', 'img-icon-5', 'rounded-1','flex-container', 'flex-justify-center', 'flex-align-center', 'text-5');
            btn_n.addEventListener('mouseenter', function(){
            btn_n.classList.remove('bg-color-2');
            btn_n.classList.add('bg-color-1');});
            btn_n.addEventListener('mousedown', function(){
            btn_n.classList.remove('bg-color-1');
            btn_n.classList.add('bg-color-2');});
            btn_n.addEventListener('mouseleave', function(){
            btn_n.classList.remove('bg-color-1');
            btn_n.classList.add('bg-color-2');});

            btn_n.textContent = value_show[var_];
            btn_n.addEventListener('mouseup', function(){
                btn_n.classList.remove('bg-color-2');
                btn_n.classList.add('bg-color-1');
                //aqui se agrega el valor respectivo al input de la formula
                in_problem.focus();
                in_problem.value = in_problem.value + element;
            });
            const div_col = document.createElement('div');
            div_col.classList.add('col-1', 'margin-left-2');
            div_col.appendChild(btn_n);
            div_row.appendChild(div_col);
            var_ += 1;
        });

    //valores de elementos
        label_problem.textContent = 'Ecuacion en funcion de "x"';
        label_x.textContent = 'Valor inicial de "x"';
        label_error.textContent = 'Error minimo deseado en porcentaje'

    //agregar elementos
        container.appendChild(label_problem);
        container.appendChild(in_problem);
        //TECLADO
        container.appendChild(container_keyboard);
        //Fin TECLADO
        container.appendChild(label_x);
        container.appendChild(in_x);
        container.appendChild(label_error);
        container.appendChild(in_error);
        container.appendChild(btn_sub);
}

keyb_();