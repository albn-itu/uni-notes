#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct Point {
  double x;
  double y;
};

double distance(struct Point p1, struct Point p2) {
  return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

int main() {
  int n;
  scanf("%d", &n);

  struct Point *points = (struct Point *)malloc(n * sizeof(struct Point));

  for (int i = 0; i < n; i++) {
    scanf("%lf %lf", &points[i].x, &points[i].y);
  }

  struct Point closest[2];
  double min_dist = distance(points[0], points[1]);

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      double d = distance(points[i], points[j]);

      if (d < min_dist) {
        min_dist = d;
        closest[0] = points[i];
        closest[1] = points[j];
      }
    }
  }

  printf("%lf %lf\n%lf %lf\n", closest[0].x, closest[0].y, closest[1].x,
         closest[1].y);

  return 0;
}
