% MUESTREAR SEÑAL 
[n , f_n] = MuestrearSenial();
size(n,2);

% HACER FFT CON MATLAB
Matlab_F = Matlab_FFT(f_n, size(n,2));

% LEER txt CON FFT de C++
Mi_FFT(size(n,2));


function [nT , xn] = MuestrearSenial()
    F = 10; %Frecuencia de entrada
    Fs = 200; %Frecuencia de muestreo y cantidad de muestras
    f = F/Fs; 
    A = 2;  %Amplitud
    Fase = 0;  %theta
    T = 1/Fs;  %Tiempo de muestreo

    %La frecuencia relativa debe estar entre -1/2 y 1/2 asi que veifico eso
    while f>(1/2)
        f = f - 1; 
    end

    %Creacion de la señal continua
    t=(0:.001:1); %Arreglo del tiempo continuo. 1001 muestras
    xt = A*cos(2*pi*F*t+Fase); %Funcion continua

    %Creacion de la señal discreta
    n = (0:Fs); % Cantidad de muestras 
    xn = A*cos(2*pi*f*n+Fase);
    nT = n*T;
    
    %Superpongo graficas
    figure(1)
    plot(t,xt,'LineWidth',1,'color','blue');
    hold on
    stem(n*T,xn,'magenta');
    grid on; 
    title('Señal Muestreada', 'color', 'blue')
    xlabel('Tiempo [s]')
    ylabel('Amplitd (Volts)')
    ylim([-2.5 2.5])
    grid

end
 
function Matlab_F = Matlab_FFT(f_n, cantMuestras)
    Matlab_F = fft(f_n,cantMuestras);
    figure(2)
    plot(f_n,abs(Matlab_F));
    % freq = fftshift(Matlab_F);  
    % plot(abs(freq));
    plot(abs(Matlab_F)/cantMuestras)
    title('MATLAB FFT', 'color', 'blue')
    xlabel('Frecuencia [Hz]')
    ylabel('Amplitd (Volts)')
    grid
end

function Mi_FFT(cantMuestras)
   %T = readtable('Xfourier.txt','ReadVariableNames',false);
    misResults = fopen('Xfourier.txt','r');
    A = textscan(misResults,'%s');
    fclose(misResults);
    A = str2double(A{1});
    B = transpose(A);
    figure(3)
    plot(abs(B)/cantMuestras)   
    title('Mi FFT', 'color', 'blue')
    xlabel('Frecuencia [Hz]')
    ylabel('Amplitd (Volts)')
    grid

end
