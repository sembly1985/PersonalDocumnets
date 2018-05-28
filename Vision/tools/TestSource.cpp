#include <Windows.h>
#include <vector>
#include "TestSource.hpp"

using namespace std;
TestSource::TestSource()
{
}


TestSource::~TestSource()
{
}

string TestSource::targetFile = "";
string TestSource::baseFold = "D:\\opencv";

bool TestSource::PathCondition(string path)
{
	string fileName = "\\"+ targetFile;
	if (path.length() > fileName.length())
		return (path.substr(path.length() - fileName.length(), fileName.length()) == fileName);
	else
		return false;
}

void TestSource::ListFilesFolds(string path, vector<string> &files, vector<string> &folds)
{
	HANDLE hFile;
	WIN32_FIND_DATA pNextInfo;
	hFile = FindFirstFile((LPCTSTR)(path.c_str()), &pNextInfo);
	while (FindNextFile(hFile, &pNextInfo))
	{
		if (pNextInfo.cFileName[0] == '.')//过滤.和..  
			continue;
		if (pNextInfo.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
		{
			folds.push_back(string(pNextInfo.cFileName));
		}
		else {
			files.push_back(string(pNextInfo.cFileName));
		}

	}
}

int TestSource::SearchFiles(string path, pFileCondition condition, vector<string> &result, int onlyFirst)
{
	vector<string> folds = vector<string>();
	vector<string> files = vector<string>();
	ListFilesFolds(path + "\\" + "*.*", files, folds);
	// check all files
	size_t i;
	for (i = 0; i < files.size(); i++)
	{
		if (condition(path + "\\" + files[i]))
		{
			result.push_back(path + "\\" + files[i]);
			if (onlyFirst)
			{
				return 1;
			}
		}
	}
	// check all folds 
	for (i = 0; i < folds.size(); i++)
	{
		if (SearchFiles(path + "\\" + folds[i], condition, result, onlyFirst) == 1)
			return 1;
	}
	return 0;
}


string TestSource::FullName(string pathName,string fileName)
{
	targetFile = fileName;
	vector<string> ret = vector<string>();
	string path = baseFold + pathName;
	SearchFiles(path, PathCondition, ret, 1);
	return ret[0];
}

vector<string> TestSource::split(const string &s, const string &seperator) {
	vector<string> result;
	typedef string::size_type string_size;
	string_size i = 0;

	while (i != s.size()) {
		//找到字符串中首个不等于分隔符的字母；
		int flag = 0;
		while (i != s.size() && flag == 0) {
			flag = 1;
			for (string_size x = 0; x < seperator.size(); ++x)
				if (s[i] == seperator[x]) {
					++i;
					flag = 0;
					break;
				}
		}

		//找到又一个分隔符，将两个分隔符之间的字符串取出；
		flag = 0;
		string_size j = i;
		while (j != s.size() && flag == 0) {
			for (string_size x = 0; x < seperator.size(); ++x)
				if (s[j] == seperator[x]) {
					flag = 1;
					break;
				}
			if (flag == 0)
				++j;
		}
		if (i != j) {
			result.push_back(s.substr(i, j - i));
			i = j;
		}
	}
	return result;
}

CmdParams TestSource::GetInput(void)
{
	CmdParams ret;
	ret.cmdStr = ""; ret.params.resize(0);
	cout << "Input Cmd strings:";
	string tmp;
	cin >> tmp;
	vector<string> tmps = TestSource::split(tmp, ",");
	ret.cmdStr = tmps[0];
	size_t i;
//	ret.params.resize(tmps.size() - 1);
	for (i = 1; i < tmps.size(); i++)
	{
		ret.params.push_back(atoi(tmps[i].c_str()));
	}
	return ret;
}