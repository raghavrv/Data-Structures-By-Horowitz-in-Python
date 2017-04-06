// https://www.codechef.com/problems/COOLING
// Find the number of pies that can be cooled

#include<iostream>
#include<new>

using namespace std;

void swap(int *ele1, int *ele2) {
    int temp = *ele2;
    *ele2 = *ele1;
    *ele1 = temp;
}

void quick_sort(int *array, int start, int end) {
    int pivot_i = end;
    int pivot = array[pivot_i];
    int cur=start;

    if (start >= end)
        return;

    if (pivot_i >= 0)
        while (cur < pivot_i) {
            if (array[cur] > array[pivot_i]) {
                array[pivot_i] = array[cur];
                array[cur] = array[pivot_i-- -1];
                array[pivot_i] = pivot;
            }
            else
                cur++;
        }

    quick_sort(array, start, pivot_i - 1);
    quick_sort(array, pivot_i + 1, end);  
}

int main() {
    int n_tries;
    int n_pies;
    int *rack_capacity, *pie_weight;
    int pie_i, rack_i;
    int max_n_pies = 0;
    bool mem_allocated = false;

    scanf("%d", &n_tries);

    while(n_tries--) {
        scanf("%d", &n_pies);
        // Allocate mem for a new int arr if the new size is lesser
        // than the previous size
        if(n_pies > max_n_pies)
            if(mem_allocated)
                // First deallocate previous block of memory
                delete[] rack_capacity;
                delete[] pie_weight;

            max_n_pies = n_pies;

            rack_capacity = new int[max_n_pies];
            pie_weight = new int[max_n_pies];
            mem_allocated = true;

        // If not overwrite the previous array
        
        for(pie_i=0; pie_i<n_pies; pie_i++)
            scanf("%d", &pie_weight[pie_i]);

        for(rack_i=0; rack_i<n_pies; rack_i++)
            scanf("%d", &rack_capacity[rack_i]);

        // Reset the indices to 0
        rack_i = 0;
        pie_i = 0;

        // Sort the racks & pies
        quick_sort(rack_capacity, 0, n_pies-1);
        quick_sort(pie_weight, 0, n_pies-1);

        // Pop one rack by one and match with pie weight
        while(rack_i < n_pies)
            if(rack_capacity[rack_i++] >= pie_weight[pie_i])
                pie_i++;

        // pie_i is the no of pies for which we've found a rack
        printf("%d\n", pie_i);

    }
    // Deallocate the memory
    delete[] rack_capacity;
    delete[] pie_weight;
}
