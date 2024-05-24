#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    int height[N];

    for (int i = 0; i < N; i++)
        cin >> height[i];

    int start = 0;
    int end = *max_element(height, height + N);
    int mid = (start + end) / 2;

    long long result;

    while (start < end)
    {
        mid = (start + end) / 2;
        result = 0;

        for (int i = 0; i < N; i++)
        {
            if (height[i] - mid > 0)
                result += height[i] - mid;
        }

        if (result >= M)
            start = mid + 1;

        else if (result < M)
            end = mid;
    }

    cout << end - 1;
    return 0;
}