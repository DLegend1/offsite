using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace SIMP
{
    public partial class Form1 : Form
    {
        public int time = 0;
        public int timer = 0;
        public Form1()
        {
            InitializeComponent();
            cbox_seconds.SelectedIndex = 0;
            cbox_minutes.SelectedIndex = 0;
            cbox_hours.SelectedIndex = 0;
            cbox_days.SelectedIndex = 0;
        }


        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }
        private void rbtn_shutdown_CheckedChanged(object sender, EventArgs e)
        {
        }
        private void rbtn_restart_CheckedChanged(object sender, EventArgs e)
        {
        }
        private void rbtn_lockscreen_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void btn_failsafe_Click(object sender, EventArgs e)
        {
        System.Diagnostics.Process.Start("Shutdown", "-a");
        }

        private void btn_start_Click(object sender, EventArgs e)
        {
            timer = cbox_seconds.SelectedIndex * 5 + cbox_minutes.SelectedIndex * 5 *60 + cbox_hours.SelectedIndex *3600 + cbox_days.SelectedIndex * 86400;
            Console.WriteLine(cbox_days.SelectedIndex);
            t_timeleft.Start();
        }

        private void cbox_seconds_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void cbox_minutes_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void cbox_hours_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void cbox_days_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void t_timeleft_Tick(object sender, EventArgs e)
        {
            time++;
            if (time >= timer)
            {
                if (rbtn_shutdown.Checked.Equals(true))
                {
                    System.Diagnostics.Process.Start("Shutdown", "-s");
                };
                if (rbtn_restart.Checked.Equals(true))
                { 
                    System.Diagnostics.Process.Start("Shutdown", "-r");
                };
                if (rbtn_lockscreen.Checked.Equals(true))
                {
                    System.Diagnostics.Process.Start("Rundll32", "User32.dll,LockWorkStation");
                }
                time = 0;
                t_timeleft.Stop();
            }
        }

        private void btn_stop_Click(object sender, EventArgs e)
        {
            time = 0;
            t_timeleft.Stop();
        }
    }
}
        // Shutdown and restart
        //Show Timer
        //int num = Convert.ToInt32(textBox1.Text);
        //textBox1.Text = Convert.ToString(num + 1);

        //Stop shutdown or restart
        //timer1.Start();