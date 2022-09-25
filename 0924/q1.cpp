

#include<iostream>
#include<climits>
#include<vector>
using namespace std;
#include<algorithm>

template <typename A, typename B>
void zip(
	const std::vector<A>& a,
	const std::vector<B>& b,
	std::vector<std::pair<A, B>>& zipped)
{
	for (size_t i = 0; i < a.size(); ++i)
	{
		zipped.push_back(std::make_pair(a[i], b[i]));
	}
}

template <typename A, typename B>
void unzip(
	const std::vector<std::pair<A, B>>& zipped,
	std::vector<A>& a,
	std::vector<B>& b)
{
	for (size_t i = 0; i < a.size(); i++)
	{
		a[i] = zipped[i].first;
		b[i] = zipped[i].second;
	}
}


class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        std::vector<std::pair<std::string, int>> zipped;
        zip(names, heights, zipped);

        // Sort the vector of pairs
        std::sort(std::begin(zipped), std::end(zipped),
            [&](const auto& a, const auto& b)
            {
                return a.second > b.second;
            });

        // Write the sorted pairs back to the original vectors
        unzip(zipped, names, heights);
        return names;

    }
};
