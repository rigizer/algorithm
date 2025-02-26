#include <stdio.h>
#include <stdlib.h>

#define MAX_N 202
#define MAX_QUEUE 40000

typedef struct {
    int type, x, y, time;
} Virus;

int N, K;
int adj[MAX_N][MAX_N];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, -1, 1};

Virus queue[MAX_QUEUE];
int front = 0, rear = 0;

int compare(const void* a, const void* b) {
    return ((Virus*)a)->type - ((Virus*)b)->type;
}

void push(Virus v) {
    queue[rear++] = v;
}

Virus pop() {
    return queue[front++];
}

int isEmpty() {
    return front == rear;
}

int main() {
    scanf("%d %d", &N, &K);
    
    Virus viruses[MAX_QUEUE];
    int virus_count = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &adj[i][j]);
            if (adj[i][j] != 0) {
                viruses[virus_count++] = (Virus){adj[i][j], i, j, 0};
            }
        }
    }

    int S, X, Y;
    scanf("%d %d %d", &S, &X, &Y);
    X--, Y--;

    qsort(viruses, virus_count, sizeof(Virus), compare);
    for (int i = 0; i < virus_count; i++) {
        push(viruses[i]);
    }

    while (!isEmpty()) {
        Virus v = pop();

        if (v.time == S) break;\

        for (int dir = 0; dir < 4; dir++) {
            int nx = v.x + dx[dir];
            int ny = v.y + dy[dir];

            if (nx >= 0 && ny >= 0 && nx < N && ny < N && adj[nx][ny] == 0) {
                adj[nx][ny] = v.type;
                push((Virus){v.type, nx, ny, v.time + 1});
            }
        }
    }

    printf("%d\n", adj[X][Y]);
    return 0;
}
