#include <stdio.h>
/**
 * Add 50 to all the elements in the array
 */
void add_fifthy (int arr[], int length) {
  for (int i=0; i < length; i++) {
    arr[i] = arr[i] + 50;
  }
}