function solution(m, n, board) {
    let cnt = 0;
    board = board.map((curr) => {
        return curr.split("")
    })
    while (true) {
        let founded = []
        for (var i = 0; i < m - 1; i++) {
            for (var j = 0; j < n - 1; j++) {
                if (board[i][j] !== 0 && board[i][j] == board[i][j + 1] && board[i][j] == board[i + 1][j] && board[i][j] == board[i + 1][j + 1]) {
                    founded.push([i, j])
                }
            }
        }
        if(founded.length == 0) {
            for (var i = 0; i < m; i++) {
                for (var j = 0; j < n; j++) {
                    if (board[i][j] == 0) {
                        cnt++;
                    }
                }
            }
            return cnt;
        }
        founded.forEach(a => {
            board[a[0]][a[1]] = 0;
            board[a[0] + 1][a[1]] = 0;
            board[a[0]][a[1] + 1] = 0;
            board[a[0] + 1][a[1] + 1] = 0
        })
        for (let i = m - 1; i > 0; i--) {
            if (! board[i].some(v => ! v)) continue;

            for (let j = 0; j < n; j++) {
                for (let k = i - 1; k >= 0 && ! board[i][j]; k--) {
                    if (board[k][j]) {
                        board[i][j] = board[k][j];
                        board[k][j] = 0;
                        break;
                    }
                }
            }
        }
    }
    
}

console.log(solution(4,5, ['AAAAA','AUUUA','AUUAA','AAAAA']))