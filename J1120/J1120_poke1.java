package J1120;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.net.URL;
import javax.imageio.ImageIO;
import java.util.*;

public class J1120_poke1 {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            try {
                UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
            } catch (Exception e) {}
            new PokemonMinesweeperUltimate().setVisible(true);
        });
    }
}

class PokemonMinesweeperUltimate extends JFrame {
    private int level = 1, maxLevel = 12;
    private int rows = 9, cols = 9, mines = 10;
    private JButton[][] cells;
    private int[][] board;
    private boolean[][] opened, flagged;
    private boolean firstClick = true, gameOver = false;
    private int flagsLeft, seconds = 0, combo = 0, totalScore = 0;
    private JLabel levelLbl, timerLbl, mineLbl, comboLbl, scoreLbl, statusLbl;
    private JPanel gamePanel, topPanel;
    private javax.swing.Timer timer;
    private Random rand = new Random();

    // 完整寶可夢資料庫（離線）
    private static final Map<Integer, Pokemon> POKE = new HashMap<>();
    static {
        POKE.put(25,  new Pokemon("皮卡丘", "電", "老鼠寶可夢，放電1000萬伏特！最可愛！", false));
        POKE.put(6,   new Pokemon("噴火龍", "火/飛行", "傳說之龍！噴射藍色烈焰！", true));
        POKE.put(150, new Pokemon("超夢", "超能力", "人造最強寶可夢！能毀滅世界！", true));
        POKE.put(384, new Pokemon("烈空坐", "龍/飛行", "天空之神！掌控天氣！", true));
        POKE.put(483, new Pokemon("帝牙盧卡", "鋼/龍", "時間之神！能凍結時間！", true));
        POKE.put(484, new Pokemon("帕路奇亞", "水/龍", "空間之神！能扭曲空間！", true));
        POKE.put(643, new Pokemon("萊希拉姆", "龍/火", "真實之龍！純白火焰！", true));
        POKE.put(716, new Pokemon("哲爾尼亞斯", "妖精", "生命之鹿！閃耀彩虹光芒！", true));
        POKE.put(888, new Pokemon("蒼響", "妖精/鋼", "英雄之劍！王者氣勢！", true));
        POKE.put(898, new Pokemon("阿爾宙斯", "一般", "創世神！創造宇宙的存在！", true));
        // 一般寶可夢
        for (int i = 1; i <= 200; i++) if (!POKE.containsKey(i)) {
            POKE.put(i, new Pokemon("第" + i + "號寶可夢", "???", "神秘的寶可夢…", false));
        }
    }

    static class Pokemon {
        String name, type, desc;
        boolean legendary;
        Pokemon(String n, String t, String d, boolean l) { name=n; type=t; desc=d; legendary=l; }
    }

    public PokemonMinesweeperUltimate() {
        setTitle("寶可夢地雷王・最終幻想版");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        setBackground(new Color(20, 20, 40));

        createTopPanel();
        restart();
        pack();
        setLocationRelativeTo(null);
        setResizable(false);
    }

    private void createTopPanel() {
        topPanel = new JPanel();
        topPanel.setBackground(new Color(20, 20, 60));
        topPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        topPanel.setLayout(new GridBagLayout());
        GridBagConstraints g = new GridBagConstraints();
        g.insets = new Insets(10, 20, 10, 20);

        levelLbl = lbl("第 1 關：新手訓練家", 36, new Color(255, 215, 0));
        timerLbl = lbl("000", 50, Color.CYAN);
        timerLbl.setFont(new Font("Consolas", Font.BOLD, 50));
        mineLbl = lbl("地雷: 10", 28, Color.PINK);
        comboLbl = lbl("Combo ×0", 28, Color.ORANGE);
        scoreLbl = lbl("分數: 0", 28, Color.YELLOW);
        statusLbl = lbl("點擊開始，第一下絕對安全！", 26, Color.LIGHT_GRAY);

        JButton restartBtn = btn("重新開始", new Color(255, 100, 100));
        restartBtn.addActionListener(e -> restart());

        JButton quitBtn = btn("退出遊戲", new Color(100, 100, 255));
        quitBtn.addActionListener(e -> System.exit(0));

        g.gridx = 0; g.gridy = 0; g.gridwidth = 3; topPanel.add(levelLbl, g);
        g.gridwidth = 1; g.gridx = 3; topPanel.add(timerLbl, g);
        g.gridx = 0; g.gridy = 1; topPanel.add(mineLbl, g);
        g.gridx = 1; topPanel.add(comboLbl, g);
        g.gridx = 2; topPanel.add(scoreLbl, g);
        g.gridx = 3; topPanel.add(restartBtn, g);
        g.gridx = 4; topPanel.add(quitBtn, g);
        g.gridx = 0; g.gridy = 2; g.gridwidth = 5; topPanel.add(statusLbl, g);

        add(topPanel, BorderLayout.NORTH);
    }

    private JLabel lbl(String text, int size, Color c) {
        JLabel l = new JLabel(text, SwingConstants.CENTER);
        l.setFont(new Font("微軟正黑體", Font.BOLD, size));
        l.setForeground(c);
        return l;
    }

    private JButton btn(String text, Color bg) {
        JButton b = new JButton(text);
        b.setFont(new Font("微軟正黑體", Font.BOLD, 20));
        b.setBackground(bg);
        b.setForeground(Color.WHITE);
        b.setFocusPainted(false);
        return b;
    }

    private void restart() {
        setLevel();
        firstClick = true; gameOver = false; seconds = 0; combo = 0; flagsLeft = mines;
        levelLbl.setText("第 " + level + " 關：" + getLevelTitle());
        timerLbl.setText("000");
        mineLbl.setText("地雷: " + mines);
        comboLbl.setText("Combo ×0");
        scoreLbl.setText("分數: " + totalScore);
        statusLbl.setText("第" + level + "關開始！第一下絕對安全！");

        if (timer != null) timer.stop();
        timer = new javax.swing.Timer(1000, e -> timerLbl.setText(String.format("%03d", ++seconds)));

        if (gamePanel != null) remove(gamePanel);
        gamePanel = createGameBoard();
        add(gamePanel, BorderLayout.CENTER);
        revalidate();
        repaint();
        pack();
    }

    private void setLevel() {
        rows = level <= 3 ? 9 : level <= 8 ? 16 : 20;
        cols = level <= 2 ? 9 : level <= 7 ? 16 : level <= 11 ? 30 : 40;
        mines = level * 12 + (level > 6 ? level * 15 : 0);
        if (mines > rows * cols * 0.23) mines = (int)(rows * cols * 0.23);
    }

    private String getLevelTitle() {
        String[] titles = {"新手訓練家","道館挑戰者","四天王候選","冠軍候選","傳說訓練家","神獸獵人","究極調查員","世界王者","阿爾宙斯認證","創世之神","宇宙霸主","超越者"};
        return titles[Math.min(level-1, titles.length-1)];
    }

    private JPanel createGameBoard() {
        JPanel panel = new JPanel(new GridLayout(rows, cols, 2, 2));
        panel.setBackground(new Color(40, 40, 80));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        cells = new JButton[rows][cols];
        board = new int[rows][cols];
        opened = new boolean[rows][cols];
        flagged = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                JButton cell = new JButton();
                cell.setPreferredSize(new Dimension(40, 40));
                cell.setBackground(new Color(100, 200, 100));
                cell.setBorder(BorderFactory.createRaisedBevelBorder());
                cell.setFocusPainted(false);
                int x = i, y = j;
                cell.addMouseListener(new MouseAdapter() {
                    public void mousePressed(MouseEvent e) {
                        if (gameOver || opened[x][y]) return;
                        if (SwingUtilities.isRightMouseButton(e)) {
                            if (!opened[x][y]) {
                                flagged[x][y] = !flagged[x][y];
                                cell.setIcon(flagged[x][y] ? getFlag() : null);
                                flagsLeft += flagged[x][y] ? -1 : 1;
                                mineLbl.setText("地雷: " + flagsLeft);
                            }
                            return;
                        }
                        if (flagged[x][y]) return;

                        if (firstClick) {
                            firstClick = false;
                            placeMines(x, y);
                            timer.start();
                        }

                        if (board[x][y] < 0) {
                            lose(x, y);
                        } else {
                            int openedCount = floodOpen(x, y);
                            combo++;
                            totalScore += openedCount * (10 + combo * 5);
                            scoreLbl.setText("分數: " + totalScore);
                            comboLbl.setText("Combo ×" + combo);
                            checkVictory();
                        }
                    }
                });
                cells[i][j] = cell;
                panel.add(cell);
            }
        }
        return panel;
    }

    private void placeMines(int safeX, int safeY) {
        int placed = 0;
        int legendary = level >= 5 ? getLegendary() : -1;
        while (placed < mines) {
            int i = rand.nextInt(rows), j = rand.nextInt(cols);
            if (board[i][j] == 0 && !(Math.abs(i-safeX)<=1 && Math.abs(j-safeY)<=1)) {
                int id = (placed == 0 && legendary != -1) ? legendary : rand.nextInt(200) + 1;
                board[i][j] = -id;
                placed++;
            }
        }
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                if (board[i][j] == 0)
                    board[i][j] = countAdjacent(i, j);
    }

    private int countAdjacent(int i, int j) {
        int cnt = 0;
        for (int x = -1; x <= 1; x++) for (int y = -1; y <= 1; y++)
            if (x != 0 || y != 0) {
                int ni = i + x, nj = j + y;
                if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && board[ni][nj] < 0) cnt++;
            }
        return cnt;
    }

    private int floodOpen(int i, int j) {
        if (i < 0 || i >= rows || j < 0 || j >= cols || opened[i][j] || flagged[i][j]) return 0;
        opened[i][j] = true;
        JButton b = cells[i][j];
        b.setEnabled(false);
        b.setBorder(BorderFactory.createLoweredBevelBorder());
        int val = board[i][j];
        int count = 1;
        if (val > 0) {
            b.setText(String.valueOf(val));
            b.setForeground(getNumberColor(val));
        } else {
            b.setBackground(new Color(220, 255, 220));
            for (int x = -1; x <= 1; x++) for (int y = -1; y <= 1; y++)
                count += floodOpen(i + x, j + y);
        }
        return count;
    }

    private void lose(int x, int y) {
        gameOver = true; timer.stop();
        combo = 0; comboLbl.setText("Combo ×0");
        int id = Math.abs(board[x][y]);
        Pokemon p = POKE.getOrDefault(id, POKE.get(25));

        for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) {
            if (board[i][j] < 0) {
                Pokemon pp = POKE.getOrDefault(Math.abs(board[i][j]), POKE.get(25));
                cells[i][j].setIcon(getIcon(Math.abs(board[i][j])));
                if (pp.legendary) cells[i][j].setBackground(Color.MAGENTA.darker());
            }
            cells[i][j].setEnabled(false);
        }

        JOptionPane.showMessageDialog(this,
            "<html><center><h1 style='color:" + (p.legendary ? "gold" : "red") + "'>" +
            (p.legendary ? "【神獸暴走！】" : "") + "你踩死了 " + p.name + "！</h1>" +
            "<p><b>屬性：</b>" + p.type + "<br><b>圖鑑：</b>" + p.desc + "</p>" +
            "<p>用時 " + seconds + " 秒　總分 " + totalScore + "</p></center></html>",
            "遊戲結束", JOptionPane.ERROR_MESSAGE, getIcon(id));
    }

    private void checkVictory() {
        for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++)
            if (board[i][j] >= 0 && !opened[i][j]) return;

        gameOver = true; timer.stop();
        totalScore += (1000 - seconds) * level * (combo + 1);
        if (level == maxLevel) {
            JOptionPane.showMessageDialog(this, "恭喜通關12關！\n你已成為宇宙最強訓練家！\n最終得分：" + totalScore,
                "世界王者！", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(this, "第" + level + "關過關！\n準備進入第" + (level+1) + "關！",
                "過關！", JOptionPane.INFORMATION_MESSAGE);
            level++;
            restart();
        }
    }

    private int getLegendary() {
        int[] gods = {6,150,384,483,484,643,716,888,898};
        return gods[rand.nextInt(gods.length)];
    }

    private ImageIcon getIcon(int id) {
        try {
            URL url = new URL("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + id + ".png");
            Image img = ImageIO.read(url).getScaledInstance(80, 80, Image.SCALE_SMOOTH);
            return new ImageIcon(img);
        } catch (Exception e) {
            return new ImageIcon();
        }
    }

    private ImageIcon getFlag() {
        try {
            URL url = new URL("https://flagcdn.com/48x36/tw.png");
            Image img = ImageIO.read(url).getScaledInstance(28, 28, Image.SCALE_SMOOTH);
            return new ImageIcon(img);
        } catch (Exception e) {
            return null;
        }
    }

    private Color getNumberColor(int n) {
        return switch (n) {
            case 1 -> Color.BLUE;      case 2 -> new Color(0,180,0);
            case 3 -> Color.RED;       case 4 -> new Color(128,0,128);
            case 5 -> new Color(139,0,0); case 6 -> new Color(0,139,139);
            case 7 -> Color.BLACK;     case 8 -> Color.GRAY;
            default -> Color.BLACK;
        };
    }
}