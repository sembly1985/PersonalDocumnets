#pragma once
#include <iostream>
#include <vector>
using namespace std;

typedef bool(*pFileCondition)(string);

typedef struct {
	string cmdStr;
	vector<int> params;
}CmdParams;

class TestSource
{
public:
	TestSource();
	~TestSource();
	static string FullName(string basePath,string fileName);
	static vector<string> split(const string &s, const string &seperator);
	static CmdParams GetInput(void);
	static string baseFold;
private:
	bool static PathCondition(string path);
	void static ListFilesFolds(string path, vector<string> &files, vector<string> &folds);
	int static SearchFiles(string path, pFileCondition condition, vector<string> &result, int onlyFirst);
	static string targetFile;

};

