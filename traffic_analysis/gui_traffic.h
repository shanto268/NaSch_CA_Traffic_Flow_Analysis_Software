#ifndef GUI_TRAFFIC_H
#define GUI_TRAFFIC_H

#include <QMainWindow>

namespace Ui {
class GUI_traffic;
}

class GUI_traffic : public QMainWindow
{
    Q_OBJECT

public:
    explicit GUI_traffic(QWidget *parent = nullptr);
    ~GUI_traffic();

private:
    Ui::GUI_traffic *ui;
};

#endif // GUI_TRAFFIC_H
