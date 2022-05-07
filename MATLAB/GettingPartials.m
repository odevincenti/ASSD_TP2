
clc
clear all
%Leo datos del archivo de audio
[datos_leidos, fm] = audioread('Flauta-SI.wav');

muestras = length(datos_leidos);

%Se normaliza la señal sobre +/-1
datos_leidos = datos_leidos/max(datos_leidos);

%Reproduce la señal guardada a la frecuencia deseada
player = audioplayer(datos_leidos,fm);
play(player);

%Grafica señal en tiempo
subplot(3,1,1)
duracion = muestras/fm;
tm=1/fm;
tiempo=linspace(0,duracion,muestras);
plot(tiempo,datos_leidos)
xlabel('Segundos')
ylabel('Señal (V)')
axis tight
grid 


%Grafico espectro en frecuencia
subplot(3,1,2)
frecuencias = linspace(0,fm,muestras);
longmed = muestras/2;
fr = abs(fft(datos_leidos))/longmed;
bar(frecuencias,fr)
axis([0 fm/2 0 0.2])
xlabel('Frecuencia [Hz]')
ylabel('Señal (Volts)')
grid

%Grafico la fase
subplot(3,1,3)
angulo = (angle(fft(datos_leidos)));
plot(frecuencias,angulo)
axis([0,fm/2, -5,5])
xlabel('Frecuencia [Hz]')
ylabel('Espectro señal Base')
grid 

%Flauta_DO(frecuencias,angulo);
%Flauta_RE(frecuencias,angulo);
%Flauta_SOL(frecuencias,angulo);
%Flauta_LA(frecuencias,angulo);
%Flauta_MI(frecuencias,angulo);
%Flauta_FA(frecuencias,angulo);
Flauta_SI(frecuencias,angulo);



%%%%%%%%%%%%%%%%%%%%%%%%%%%  FUNCIONES  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DO = C4
function Flauta_DO(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 262.478;
    A0 = 0.116309;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 524.348;
    A1 = 0.168898;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 = 786.827;
    A2 = 0.0589462;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 1008.7;
    A3 = 0.022478;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    f4 = 1310.87;
    A4 = 0.0226836;
    ph4 = estimo_fase(f4,frecuencias,angulo);

    f5 = 1579.13;
    A5 = 0.0084595;
    ph5 = estimo_fase(f5,frecuencias,angulo);

    f6 = 1841.61;
    A6 = 0.00674346;
    ph6 = estimo_fase(f6,frecuencias,angulo);

    f7 = 2103.78;
    A7 = 0.00975894;
    ph7 = estimo_fase(f7,frecuencias,angulo);
    
    Parcial = [0 ;1 ;2; 3; 4; 5; 6; 7];
    Frecuencia = [f0 ;f1; f2; f3 ;f4; f5; f6 ; f7];
    Amplitud = [A0 ; A1; A2; A3; A4; A5; A6; A7];
    Fase = [ph0 ;ph1 ;ph2 ;ph3 ;ph4 ;ph5; ph6; ph7];
    
    %%%%% Exporto datos en forma de tabla%%%%%%%
    % Parcial   Frecuencia   Amplitud   Fase  %
    %    0          f0         A0        ph0  %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    T = table(Parcial, Frecuencia, Amplitud, Fase);
    writetable(T,'Parciales_Flauta_SOL.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_SOL.txt
end

% SOL = 
function Flauta_SOL(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 392.757;
    A0 = 0.288027;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 785.514;
    A1 = 0.0931436;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 =1184.02;
    A2 = 0.0249284;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 1582.53;
    A3 = 0.0220012;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    f4 = 1976.25;
    A4 = 0.0226836;
    ph4 = estimo_fase(f4,frecuencias,angulo);

    f5 = 2374.76;
    A5 = 0.00533475;
    ph5 = estimo_fase(f5,frecuencias,angulo);

    f6 = 2761.76;
    A6 = 0.00100682;
    ph6 = estimo_fase(f6,frecuencias,angulo);

    f7 = 3151.64;
    A7 = 0.000659172;
    ph7 = estimo_fase(f7,frecuencias,angulo);
    
    Parcial = [0 ;1 ;2; 3; 4; 5; 6; 7];
    Frecuencia = [f0 ;f1; f2; f3 ;f4; f5; f6 ; f7];
    Amplitud = [A0 ; A1; A2; A3; A4; A5; A6; A7];
    Fase = [ph0 ;ph1 ;ph2 ;ph3 ;ph4 ;ph5; ph6; ph7];
    
    %%%%% Exporto datos en forma de tabla %%%%%%
    % Parcial   Frecuencia   Amplitud   Fase   %
    %    0          f0         A0        ph0   %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    T = table(Parcial, Frecuencia, Amplitud, Fase);

    writetable(T,'Parciales_Flauta_DO.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_DO.txt
end

%LA = 
function Flauta_LA(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 439.82;
    A0 = 0.109881;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 879.64;
    A1 = 0.0840688;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 = 1319.46;
    A2 = 0.0336143;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 1754.28;
    A3 = 0.0297722;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    Parcial = [0 ;1 ;2; 3];
    Frecuencia = [f0 ;f1; f2; f3];
    Amplitud = [A0 ; A1; A2; A3];
    Fase = [ph0 ;ph1 ;ph2 ;ph3];
    
    %%%%% Exporto datos en forma de tabla%%%%%%%
    % Parcial   Frecuencia   Amplitud   Fase  %
    %    0          f0         A0        ph0  %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    T = table(Parcial, Frecuencia, Amplitud, Fase);
    writetable(T,'Parciales_Flauta_LA.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_LA.txt
end

%MI = 
function Flauta_MI(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 329.263;
    A0 = 0.0705014;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 658.621;
    A1 = 0.130909;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 = 987.978;
    A2 = 0.177305;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 1317.24;
    A3 = 0.0312067;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    f4 = 1652.08;
    A4 = 0.0413316;
    ph4 = estimo_fase(f4,frecuencias,angulo);

    f5 = 1975.67;
    A5 = 0.0132167;
    ph5 = estimo_fase(f5,frecuencias,angulo);

    f6 = 2305.03;
    A6 = 0.00726571;
    ph6 = estimo_fase(f6,frecuencias,angulo);

    f7 = 2634.39;
    A7 = 0.00732285;
    ph7 = estimo_fase(f7,frecuencias,angulo);
    
    Parcial = [0 ;1 ;2; 3; 4; 5; 6; 7];
    Frecuencia = [f0 ;f1; f2; f3 ;f4; f5; f6 ; f7];
    Amplitud = [A0 ; A1; A2; A3; A4; A5; A6; A7];
    Fase = [ph0 ;ph1 ;ph2 ;ph3 ;ph4 ;ph5; ph6; ph7];
    %%%%% Exporto datos en forma de tabla%%%%%%%
    % Parcial   Frecuencia   Amplitud   Fase  %
    %    0          f0         A0        ph0  %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    T = table(Parcial, Frecuencia, Amplitud, Fase);
    writetable(T,'Parciales_Flauta_MI.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_MI.txt
end

%RE = 
function Flauta_RE(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 145.909;
    A0 = 0.0843676;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 291.461;
    A1 = 0.148307;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 = 437.726;
    A2 = 0.128777;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 588.261;
    A3 = 0.0379503;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    f4 = 729.543;
    A4 = 0.0289062;
    ph4 = estimo_fase(f4,frecuencias,angulo);

    f5 = 875.808;
    A5 = 0.0290701;
    ph5 = estimo_fase(f5,frecuencias,angulo);

    f6 = 1020.29;
    A6 = 0.015433;
    ph6 = estimo_fase(f6,frecuencias,angulo);

    f7 = 1167.27;
    A7 = 0.0159474;
    ph7 = estimo_fase(f7,frecuencias,angulo);
    
    Parcial = [0 ;1 ;2; 3; 4; 5; 6; 7];
    Frecuencia = [f0 ;f1; f2; f3 ;f4; f5; f6 ; f7];
    Amplitud = [A0 ; A1; A2; A3; A4; A5; A6; A7];
    Fase = [ph0 ;ph1 ;ph2 ;ph3 ;ph4 ;ph5; ph6; ph7];
    %%%%% Exporto datos en forma de tabla%%%%%%%
    % Parcial   Frecuencia   Amplitud   Fase  %
    %    0          f0         A0        ph0  %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    T = table(Parcial, Frecuencia, Amplitud, Fase);
    writetable(T,'Parciales_Flauta_RE.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_RE.txt
end

%FA = 
function Flauta_FA(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 174.05;
    A0 = 0.127015;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 347.408;
    A1 = 0.165755;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 = 512.111;
    A2 = 0.116984;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 588.261;
    A3 = 0.0379503;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    f4 = 695.161;
    A4 = 0.0472083;
    ph4 = estimo_fase(f4,frecuencias,angulo);

    f5 = 868.519;
    A5 = 0.0106281;
    ph5 = estimo_fase(f5,frecuencias,angulo);

    f6 = 1042.22;
    A6 = 0.0150688;
    ph6 = estimo_fase(f6,frecuencias,angulo);

    f7 = 1216.27;
    A7 = 0.0108262;
    ph7 = estimo_fase(f7,frecuencias,angulo);
    
    Parcial = [0 ;1 ;2; 3; 4; 5; 6; 7];
    Frecuencia = [f0 ;f1; f2; f3 ;f4; f5; f6 ; f7];
    Amplitud = [A0 ; A1; A2; A3; A4; A5; A6; A7];
    Fase = [ph0 ;ph1 ;ph2 ;ph3 ;ph4 ;ph5; ph6; ph7];
    %%%%% Exporto datos en forma de tabla%%%%%%%
    % Parcial   Frecuencia   Amplitud   Fase  %
    %    0          f0         A0        ph0  %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    T = table(Parcial, Frecuencia, Amplitud, Fase);
    writetable(T,'Parciales_Flauta_FA.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_FA.txt
end

%SI = 
function Flauta_SI(frecuencias, angulo)
    %Obtengo valores de parciales
    %De inspeccion las frecuencias de los parciales son:
    f0 = 246.995;
    A0 = 0.413717;
    ph0 = estimo_fase(f0,frecuencias,angulo);

    f1 = 497.749;
    A1 = 0.0126027;
    ph1 = estimo_fase(f1,frecuencias,angulo);

    f2 = 745.871;
    A2 = 0.0227882;
    ph2 = estimo_fase(f2,frecuencias,angulo);

    f3 = 991.738;
    A3 = 0.0324735;
    ph3 = estimo_fase(f3,frecuencias,angulo);

    f4 = 1242.87;
    A4 = 0.0155078;
    ph4 = estimo_fase(f4,frecuencias,angulo);

    f5 = 1489.11;
    A5 = 0.00725913;
    ph5 = estimo_fase(f5,frecuencias,angulo);

    f6 = 1735.35;
    A6 = 0.0042306;
    ph6 = estimo_fase(f6,frecuencias,angulo);

    Parcial = [0 ;1 ;2; 3; 4; 5; 6];
    Frecuencia = [f0 ;f1; f2; f3 ;f4; f5; f6];
    Amplitud = [A0 ; A1; A2; A3; A4; A5; A6];
    Fase = [ph0 ;ph1 ;ph2 ;ph3 ;ph4 ;ph5; ph6];
    %%%%% Exporto datos en forma de tabla%%%%%%%
    % Parcial   Frecuencia   Amplitud   Fase  %
    %    0          f0         A0        ph0  %                  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    T = table(Parcial, Frecuencia, Amplitud, Fase);
    writetable(T,'Parciales_Flauta_SI.txt','Delimiter', '\t','WriteRowNames', true);
    type Parciales_Flauta_SI.txt
end

function fase = estimo_fase(frecuencia,frecuencias,angulo)
    [~,idx] = min(abs(frecuencias- frecuencia));
    fase = angulo(idx);
end

