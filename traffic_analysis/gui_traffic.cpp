#include "gui_traffic.h"
#include "ui_gui_traffic.h"

GUI_traffic::GUI_traffic(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::GUI_traffic)
{
    ui->setupUi(this);
}

GUI_traffic::~GUI_traffic()
{
    delete ui;
}
