#use heap to store pair<nums[i],i> where that pq store max value on its top 

vector<int> resh(vector<int>& nums, int k)
{
  priority_queue<pair<int,int>> heap;
  vector<int> ans;
  for(int i =0;i<nums.size();++i)
  {
    while(!heap.empty && heap.top().second<=(i-k))
    {
      heap.pop();
    }
    heap.push(make_pair(nums[i],i));
    if (i>=k-1)
    {
      ans.push_back(heap.top().first);
    }
    return ans;
  }

}
