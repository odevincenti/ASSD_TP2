#pragma once
#include <complex>
#include <vector>
#include<cstdlib>
#include<cmath>
#include<iostream>

using namespace std;

class FastFourierTransform
{
public:
	void FFT_1(vector<double>& f, vector<complex<double>>& F);
	void FFT_2(vector<double>& f, vector<complex<double>>& F);
	void FFT_2REC(vector<complex<double>>& x, size_t N);


private:
	void CheckSize(size_t N, vector<double>& f, vector<complex<double>>& F);
	int bitreverse(int n, int B);

	vector<complex<double>> WN;

	std::complex<double> Yn;
	std::complex<double> Zn;
	std::complex<double> Tn;
	std::complex<double> WNAux;

	int realN;
	int rFin;
	int G;
	int Mari;



};

