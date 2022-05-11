#include "FFT.h"

#include <fstream>
#include <iostream>
#include <filesystem>
#include <vector>
#include <string>

using namespace std;


int main() {

	int MUESTRAS = 1000;

	/* Busco la señal f(n) con N muestras*/
	ifstream f_n_txt;
	f_n_txt.open("xn_" + to_string(MUESTRAS) + "_muestras.txt", ios::in);
	string line;


	if (f_n_txt.is_open())
	{

		vector<double> f;
		vector<complex<double>> F;

		while (getline(f_n_txt, line))
		{
			//aca le cargo los valores a el vector f(n)
			f.push_back(stof(line));
		}

		/* CALCULADORA DE TRANSFORMADA DE FOURIER DE f(n)*/
		
		FastFourierTransform SenalOne;
		//SenalOne.FFT_1(f, F);
		SenalOne.FFT_2(f, F);

		ofstream F_f_txt;
		int k;
		F_f_txt.open("Xfourier_" + to_string(MUESTRAS) + ".txt", ios::out);
		if (F_f_txt.is_open())
		{
			for (k = 0; k <= F.size()-1; k++)
			{
				F_f_txt << F[k].real() << "+" << F[k].imag() << "i\n";
				cout << F[k].real() << " " << F[k].imag() << "\n";
			}
		}
		
	}


}