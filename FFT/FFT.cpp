#include "FFT.h"

#ifndef PI
#define PI (3.141592653589793238463)
#endif 


void FastFourierTransform::FFT_1(vector<double>& f, vector<complex<double>>& F)
{
	/*Primer paso: Verificamos que el tamaño sea de potencias de 2 y llenamos de ceros si no lo es*/
	cout << "Checking size...\n \n";
	CheckSize(f.size(), f, F);


	/*Segundo paso: Calculamos de antemano las primeras N/2 potencias del factor W y almacenamos en Wn*/
	cout << "Calculating Wn... \n \n";
	for (size_t j = 0; j < realN / 2; j++)
	{
		complex<double> newWn = exp(complex<double>(0.0, 1.0) * complex<double>(2.0 * j * PI / realN));
		WN.push_back(newWn);
	}

	/*Tercer Paso: Calculo  de las mariposas, vamos dividiendo en 2 a N hasta que llegamos a grupos de a 2*/
		//Contadores
			//Etapas
	rFin = log2(realN);  //N es una potencia de 2 gracias a checksize
	//Grupos 
	G = 1;
	// Mariposas
	Mari = realN / 2;
	//Aux
	int g, m, r, WNindex, index1, index2;

	for (r = 1; r <= rFin; r++)   //Etapas
	{
		cout << "Calculando butterflies... Etapa " << r << "\n";
		for (g=1; g <= G; g++)  //Grupos por etapa (se multiplica por 2 cada vez q avanzo 1 etapa)
		{
			for (m = 1; m <= Mari; m++)
			{
				Yn = f[m + 2 * Mari * (g - r)];
				Zn = f[m + 2 * Mari * (g - r) + realN / (2 ^ r)];
				//Obtengo el coef WN del vector que hice antes en el paso 2 y leo en bit reverse
				WNindex = 1 + bitreverse(2 * (g - r), rFin);
				WNAux = WN[WNindex];
				Tn = Zn * WNAux;

				//Obtuve dos valores de la FFT
				index1 = m + 2 * Mari * (g - r);
				F[index1] = Yn + Tn;

				index2 = m + 2 * Mari * (g - r) + realN / (2 ^ r);
				F[index2] = Yn - Tn;  //Pues simetria

			}
		}
		//Actualizo	Mari (divido a la mitad) y el grupo r (duplico)
		Mari = Mari / 2;
		G = G * 2;
	}

}

void FastFourierTransform::FFT_2(vector<double>& f, vector<complex<double>>& F)
{
	cout << "Checking size...\n \n";
	CheckSize(f.size(), f, F);

	//Con esta version me baso en el algoritmo de Cooley-Tukey 
	// https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
	// Make copy of array and apply window
	for (int i = 0; i < realN; i++) {
		F[i] = std::complex<double>(f[i], 0);
		F[i] *= 1; // Window
	}

	// Start recursion
	FFT_2REC(F, realN);
}

void FastFourierTransform::FFT_2REC(vector<complex<double>>& x, size_t N)
{
	//Caso no recursivo --> Ya separe lo suficiente
	if (N <= 1)
	{
		return;
	}

	//Separo en PAR e IMPAR
	vector<complex<double>> PAR;
	vector<complex<double>> IMPAR;
	for (int i = 0; i < N / 2; i++)
	{
		PAR.push_back(x[i * 2]);
		IMPAR.push_back(x[i * 2 + 1]);
	}


	//Caso recursivo --> Tengo que separar en 2 otra vez
	FFT_2REC(PAR, N / 2);
	FFT_2REC(IMPAR, N / 2);

	//Calculo DFT
	for (int k = 0; k < N / 2; k++)
	{
		complex<double> T = exp(complex<double>(0, -2 * PI * k / N)) * IMPAR[k];
		x[k] = PAR[k] + T;
		x[N / 2 + k] = PAR[k] - T;
	}

}

void FastFourierTransform::CheckSize(size_t N, vector<double>& f, vector<complex<double>>& F)
{
	if (!(log2(N) == floor(log2(N)))) /* Si no es una potencia de dos tengo que convertirlo*/
	{
		int j;
		size_t NewN = N;

		for (j = 0; int((NewN / 2)) != 0; j++) {
			NewN = NewN / 2;

		}  /* cuando la división N/2 de menor a 1 --> int --> 0*/


		cout << "Tamano original: " << N << "\n";
		cout << "Tamano modificado: " << pow(2, j + 1) << "\n \n \n";

		/* Ahora resizeo el vector de las muestras de la funcion f(n) y relleno con 0*/
		f.resize(pow(2, j + 1), 0.0);
		realN = f.size();
		F.resize(pow(2, j + 1), 0.0);
	}

}

int FastFourierTransform::bitreverse(int n, int B)
{
	int m, r;

	for (r = 0, m = B - 1; m >= 0; m--)
		if ((n > m) == 1)
		{
			r += 1 << (B - 1 - m);
			n -= 1 << (m);
		}
	return(r);
}
