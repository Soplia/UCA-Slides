#include <iostream>
#include <cstdlib>
using namespace std;

class LifeRule
{
public:
	//初始化，size是二维数组的大小
	LifeRule(int size);
	//初始化，使用arr进行初始化
	LifeRule(int size, int  a[][5]);
	//析构函数，因为有指针
	~LifeRule();
	//初始化数据值为0
	void InitValue();
	//type =1 仅仅显示_state, type =2 仅仅显示_neigh， type = 3两者都进行显示
	void Display(int type);
	//_state[x][y] = aim
	void ChangeState(int x, int y, int aim);
	// 根据type的不同对_state[x][y]的邻居进行计数
	void CountNeighbour(int x, int y, int type); // 1:Without ; 2: with
	//对_state整体的邻居进行计数
	void  ChangeNeighbourWhole(int type);// 1:Without ; 2: with
	//更改_state整体
	void ChangeStateWhole();
	//计算_state[x][y]的状态
	int CalculateState(int x, int y);
	//更新_state[x][y]的状态
	void SetState(int x, int y);
	//确定x是否越界
	bool InBound(int x);
	//x: 仿真次数； type：是否有trous; typeOfDis 是何种显示类型
	void Simulation(int x, int type, int typeOfDis);// 1:Without ; 2: with
	//置_neigh为0
	void ClearNeigh();
public:
	//存放状态
	int **_state;
	//存放邻居数量
	int **_neigh;
	//存放数组的大小
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
		default: cout << "Input the right type (1、2、3) :" << endl;
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
				if (_state[tempX][tempY])//1: 有人；0: 没人
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
				if (_state[tempX][tempY])//1: 有人；0: 没人
					_neigh[x][y]++;

			}
		}
	}
	if(_state[x][y])
		_neigh[x][y]--; //除去自己
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
	//不能连接时到8不会再改变
	//能够连接时到20为一个周期
	t->Simulation(20, 2, 3);
	system("pause");
	return 0;
}
