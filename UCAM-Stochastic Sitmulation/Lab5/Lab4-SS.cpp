#include <iostream>
#include <cstdlib>
using namespace std;

class LifeRule
{
public:
	//��ʼ����size�Ƕ�ά����Ĵ�С
	LifeRule(int size);
	//��ʼ����ʹ��arr���г�ʼ��
	LifeRule(int size, int  a[][5]);
	//������������Ϊ��ָ��
	~LifeRule();
	//��ʼ������ֵΪ0
	void InitValue();
	//type =1 ������ʾ_state, type =2 ������ʾ_neigh�� type = 3���߶�������ʾ
	void Display(int type);
	//_state[x][y] = aim
	void ChangeState(int x, int y, int aim);
	// ����type�Ĳ�ͬ��_state[x][y]���ھӽ��м���
	void CountNeighbour(int x, int y, int type); // 1:Without ; 2: with
	//��_state������ھӽ��м���
	void  ChangeNeighbourWhole(int type);// 1:Without ; 2: with
	//����_state����
	void ChangeStateWhole();
	//����_state[x][y]��״̬
	int CalculateState(int x, int y);
	//����_state[x][y]��״̬
	void SetState(int x, int y);
	//ȷ��x�Ƿ�Խ��
	bool InBound(int x);
	//x: ��������� type���Ƿ���trous; typeOfDis �Ǻ�����ʾ����
	void Simulation(int x, int type, int typeOfDis);// 1:Without ; 2: with
	//��_neighΪ0
	void ClearNeigh();
public:
	//���״̬
	int **_state;
	//����ھ�����
	int **_neigh;
	//�������Ĵ�С
	int _size;
};

LifeRule::LifeRule(int size, int a[][5])
{
	_size = size;
	_state = new int *[size];
	for (int i = 0; i < _size; i++)
		_state[i] = new int[_size];

	_neigh = new int *[size];
	for (int i = 0; i < _size; i++)
		_neigh[i] = new int[_size];

	InitValue();

	for (int i = 0; i < _size; i++)
		for (int j = 0; j < _size; j++)
			_state[i][j] = a[i][j];
}

LifeRule::LifeRule(int size)
{
	_size = size;
	_state = new int *[size];
	for (int i = 0; i < _size; i++)
		_state[i] = new int[_size];

	_neigh = new int *[size];
	for (int i = 0; i < _size; i++)
		_neigh[i] = new int[_size];

	InitValue();
}

void LifeRule::InitValue()
{
	for (int i = 0; i < _size; i++)
		for (int j = 0; j < _size; j++)
		{
			_state[i][j] = 0;
			_neigh[i][j] = 0;
		}
}

LifeRule::~LifeRule()
{
	for (int i = 0; i < _size; i++)
	{
		delete[] _state[i];
		delete[] _neigh[i];
	}
	delete[] _state;
	delete[] _neigh;
}

void LifeRule::Display(int type)
{
	switch (type)
	{
		case 1:
		{
			cout << "The contents of _state:" << endl;
			for (int i = 0; i < _size; i++)
			{
				for (int j = 0; j < _size; j++)
					cout << _state[i][j] << " ";
				cout << endl;
			}
		}break;
		case 2:
		{
			cout << "The contents of _neigh:" << endl;
			for (int i = 0; i < _size; i++)
			{
				for (int j = 0; j < _size; j++)
					cout << _neigh[i][j] << " ";
				cout << endl;
			}
		}break;
		case 3:
		{
			cout << "The contents of _state & _neigh:" << endl;
			for (int i = 0; i < _size; i++)
			{
				for (int j = 0; j < _size; j++)
					cout << _state[i][j] << " ";
				cout << endl;
			}
			cout << endl;
			for (int i = 0; i < _size; i++)
			{
				for (int j = 0; j < _size; j++)
					cout << _neigh[i][j] << " ";
				cout << endl;
			}
			system("pause");
			system("cls");

		}break;
		default: cout << "Input the right type (1��2��3) :" << endl;
	}
}

void LifeRule::ChangeState(int x, int y, int aim)
{
	_state[x][y] = aim;
}

bool LifeRule::InBound(int x)
{
	return (x >= 0 && x < _size);
}

void LifeRule::CountNeighbour(int x, int y, int type)
{
	for (int i = 0; i <= 2; i++)
	{
		int tempX = x - 1;
		tempX += i;
		if (type == 1)
		{
			//cout << "tempX = " << tempX << endl;
			if (!InBound(tempX))
				continue;
		}
		else if (type == 2)
		{
			if (tempX == -1)
				tempX = _size - 1;
			else if (tempX == _size)
				tempX = 0;
			if (!InBound(tempX))
				continue;
		}

		for (int j = 0; j <= 2; j++)
		{
			int tempY = y - 1;
			tempY += j;
			if (type == 1)
			{
				if (!InBound(tempY))
					continue;
				if (_state[tempX][tempY])//1: ���ˣ�0: û��
					_neigh[x][y]++;
			}
			else if (type == 2)
			{
				if (tempY == -1)
					tempY = _size - 1;
				else if (tempY == _size)
					tempY = 0;
				if (!InBound(tempY))
					continue;
				if (_state[tempX][tempY])//1: ���ˣ�0: û��
					_neigh[x][y]++;

			}
		}
	}
	if(_state[x][y])
		_neigh[x][y]--; //��ȥ�Լ�
}

void LifeRule::SetState(int x, int y)
{
	_state[x][y] = CalculateState(x, y);
}

int LifeRule::CalculateState(int x, int y)
{
	if (_state[x][y])
		return _neigh[x][y] >= 2 && _neigh[x][y] <= 3 ? 1 : 0;
	else if (!_state[x][y])
		return _neigh[x][y] == 3;
}

void LifeRule::ChangeNeighbourWhole(int type)
{
	for (int i = 0; i < _size; i++)
		for (int j = 0; j < _size; j++)
			CountNeighbour(i, j, type);
}

void LifeRule::ChangeStateWhole()
{
	for (int i = 0; i < _size; i++)
		for (int j = 0; j < _size; j++)
			SetState(i, j);
}

void LifeRule::Simulation(int times, int type, int typeOfDis)
{
	for (int i = 0; i < times; i++)
	{
		ClearNeigh();
		ChangeNeighbourWhole(type);
		ChangeStateWhole();
		cout << i + 1 << "th :";
		Display(typeOfDis);
	}
}

void LifeRule::ClearNeigh()
{
	for (int i = 0; i < _size; i++)
		for (int j = 0; j < _size; j++)
			_neigh[i][j] = 0;
}

int main()
{
	const int initSize = 5;
	int initArr[][initSize] = 
	{
		0, 0, 0, 0, 0,
		0, 0, 1, 0, 0,
		0, 0, 0, 1, 0,
		0, 1, 1, 1, 0,
		0, 0, 0, 0, 0,
	};

	LifeRule *t =new  LifeRule(initSize,  initArr);
	cout << "The inital state :" << endl;
	t->Display(3);
	cout << endl;
	//��������ʱ��8�����ٸı�
	//�ܹ�����ʱ��20Ϊһ������
	t->Simulation(20, 2, 3);
	system("pause");
	return 0;
}
