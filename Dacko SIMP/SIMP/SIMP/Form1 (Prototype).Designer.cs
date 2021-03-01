namespace SIMP
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.cbox_seconds = new System.Windows.Forms.ComboBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rbtn_lockscreen = new System.Windows.Forms.RadioButton();
            this.rbtn_restart = new System.Windows.Forms.RadioButton();
            this.rbtn_shutdown = new System.Windows.Forms.RadioButton();
            this.btn_failsafe = new System.Windows.Forms.Button();
            this.btn_start = new System.Windows.Forms.Button();
            this.cbox_minutes = new System.Windows.Forms.ComboBox();
            this.cbox_hours = new System.Windows.Forms.ComboBox();
            this.cbox_days = new System.Windows.Forms.ComboBox();
            this.t_timeleft = new System.Windows.Forms.Timer(this.components);
            this.btn_stop = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // cbox_seconds
            // 
            this.cbox_seconds.AccessibleName = "cbox_seconds";
            this.cbox_seconds.FormattingEnabled = true;
            this.cbox_seconds.Items.AddRange(new object[] {
            "0 second",
            "5 seconds",
            "10 seconds",
            "15 seconds",
            "20 seconds",
            "25 seconds",
            "30 seconds",
            "35 seconds",
            "40 seconds",
            "45 seconds",
            "50 seconds",
            "55 seconds"});
            this.cbox_seconds.Location = new System.Drawing.Point(507, 47);
            this.cbox_seconds.Name = "cbox_seconds";
            this.cbox_seconds.Size = new System.Drawing.Size(121, 24);
            this.cbox_seconds.TabIndex = 0;
            this.cbox_seconds.SelectedIndexChanged += new System.EventHandler(this.cbox_seconds_SelectedIndexChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rbtn_lockscreen);
            this.groupBox1.Controls.Add(this.rbtn_restart);
            this.groupBox1.Controls.Add(this.rbtn_shutdown);
            this.groupBox1.Location = new System.Drawing.Point(84, 166);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(306, 152);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "groupBox1";
            this.groupBox1.Enter += new System.EventHandler(this.groupBox1_Enter);
            // 
            // rbtn_lockscreen
            // 
            this.rbtn_lockscreen.AccessibleName = "rbtn_lockscreen";
            this.rbtn_lockscreen.AutoSize = true;
            this.rbtn_lockscreen.Location = new System.Drawing.Point(24, 97);
            this.rbtn_lockscreen.Name = "rbtn_lockscreen";
            this.rbtn_lockscreen.Size = new System.Drawing.Size(108, 21);
            this.rbtn_lockscreen.TabIndex = 5;
            this.rbtn_lockscreen.TabStop = true;
            this.rbtn_lockscreen.Text = "Lock Screen";
            this.rbtn_lockscreen.UseVisualStyleBackColor = true;
            this.rbtn_lockscreen.CheckedChanged += new System.EventHandler(this.rbtn_lockscreen_CheckedChanged);
            // 
            // rbtn_restart
            // 
            this.rbtn_restart.AccessibleName = "rbtn_restart";
            this.rbtn_restart.AutoSize = true;
            this.rbtn_restart.Location = new System.Drawing.Point(24, 70);
            this.rbtn_restart.Name = "rbtn_restart";
            this.rbtn_restart.Size = new System.Drawing.Size(75, 21);
            this.rbtn_restart.TabIndex = 5;
            this.rbtn_restart.TabStop = true;
            this.rbtn_restart.Text = "Restart";
            this.rbtn_restart.UseVisualStyleBackColor = true;
            this.rbtn_restart.CheckedChanged += new System.EventHandler(this.rbtn_restart_CheckedChanged);
            // 
            // rbtn_shutdown
            // 
            this.rbtn_shutdown.AccessibleName = "rbtn_shutdown";
            this.rbtn_shutdown.AutoSize = true;
            this.rbtn_shutdown.Location = new System.Drawing.Point(24, 43);
            this.rbtn_shutdown.Name = "rbtn_shutdown";
            this.rbtn_shutdown.Size = new System.Drawing.Size(91, 21);
            this.rbtn_shutdown.TabIndex = 3;
            this.rbtn_shutdown.TabStop = true;
            this.rbtn_shutdown.Text = "Shutdown";
            this.rbtn_shutdown.UseVisualStyleBackColor = true;
            this.rbtn_shutdown.CheckedChanged += new System.EventHandler(this.rbtn_shutdown_CheckedChanged);
            // 
            // btn_failsafe
            // 
            this.btn_failsafe.AccessibleName = "btn_failsafe";
            this.btn_failsafe.Location = new System.Drawing.Point(510, 236);
            this.btn_failsafe.Name = "btn_failsafe";
            this.btn_failsafe.Size = new System.Drawing.Size(118, 82);
            this.btn_failsafe.TabIndex = 3;
            this.btn_failsafe.Text = "Failsafe";
            this.btn_failsafe.UseVisualStyleBackColor = true;
            this.btn_failsafe.Click += new System.EventHandler(this.btn_failsafe_Click);
            // 
            // btn_start
            // 
            this.btn_start.AccessibleName = "btn_start";
            this.btn_start.Location = new System.Drawing.Point(510, 159);
            this.btn_start.Name = "btn_start";
            this.btn_start.Size = new System.Drawing.Size(118, 71);
            this.btn_start.TabIndex = 4;
            this.btn_start.Text = "Start";
            this.btn_start.UseVisualStyleBackColor = true;
            this.btn_start.Click += new System.EventHandler(this.btn_start_Click);
            // 
            // cbox_minutes
            // 
            this.cbox_minutes.AccessibleName = "cbox_minutes";
            this.cbox_minutes.FormattingEnabled = true;
            this.cbox_minutes.Items.AddRange(new object[] {
            "0 minutes",
            "5 minutes",
            "10 minutes",
            "15 minutes",
            "20 minutes",
            "25 minutes",
            "30 minutes",
            "35 minutes",
            "40 minutes",
            "45 minutes",
            "50 minutes",
            "55 minutes"});
            this.cbox_minutes.Location = new System.Drawing.Point(375, 47);
            this.cbox_minutes.Name = "cbox_minutes";
            this.cbox_minutes.Size = new System.Drawing.Size(121, 24);
            this.cbox_minutes.TabIndex = 5;
            this.cbox_minutes.SelectedIndexChanged += new System.EventHandler(this.cbox_minutes_SelectedIndexChanged);
            // 
            // cbox_hours
            // 
            this.cbox_hours.AccessibleName = "cbox_hours";
            this.cbox_hours.FormattingEnabled = true;
            this.cbox_hours.Items.AddRange(new object[] {
            "0 hours",
            "1 hour",
            "2 hours",
            "3 hours",
            "4 hours",
            "5 hours",
            "6 hours",
            "7 hours",
            "8 hours",
            "9 hours",
            "10 hours",
            "11 hours",
            "12 hours",
            "13 hours",
            "14 hours",
            "15 hours",
            "16 hours",
            "17 hours",
            "18 hours",
            "19 hours",
            "20 hours",
            "21 hours",
            "22 hours",
            "23 hours"});
            this.cbox_hours.Location = new System.Drawing.Point(248, 47);
            this.cbox_hours.Name = "cbox_hours";
            this.cbox_hours.Size = new System.Drawing.Size(121, 24);
            this.cbox_hours.TabIndex = 6;
            this.cbox_hours.SelectedIndexChanged += new System.EventHandler(this.cbox_hours_SelectedIndexChanged);
            // 
            // cbox_days
            // 
            this.cbox_days.AccessibleName = "cbox_days";
            this.cbox_days.FormattingEnabled = true;
            this.cbox_days.Items.AddRange(new object[] {
            "0 Days",
            "1 Day",
            "2 Days",
            "3 Days",
            "4 Days",
            "5 Days",
            "6 Days",
            "7 Days"});
            this.cbox_days.Location = new System.Drawing.Point(121, 47);
            this.cbox_days.Name = "cbox_days";
            this.cbox_days.Size = new System.Drawing.Size(121, 24);
            this.cbox_days.TabIndex = 7;
            this.cbox_days.SelectedIndexChanged += new System.EventHandler(this.cbox_days_SelectedIndexChanged);
            // 
            // t_timeleft
            // 
            this.t_timeleft.Interval = 1000;
            this.t_timeleft.Tick += new System.EventHandler(this.t_timeleft_Tick);
            // 
            // btn_stop
            // 
            this.btn_stop.AccessibleName = "btn_stop";
            this.btn_stop.Location = new System.Drawing.Point(655, 159);
            this.btn_stop.Name = "btn_stop";
            this.btn_stop.Size = new System.Drawing.Size(133, 71);
            this.btn_stop.TabIndex = 8;
            this.btn_stop.Text = "Stop";
            this.btn_stop.UseVisualStyleBackColor = true;
            this.btn_stop.Click += new System.EventHandler(this.btn_stop_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btn_stop);
            this.Controls.Add(this.cbox_days);
            this.Controls.Add(this.cbox_hours);
            this.Controls.Add(this.cbox_minutes);
            this.Controls.Add(this.btn_start);
            this.Controls.Add(this.btn_failsafe);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.cbox_seconds);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ComboBox cbox_seconds;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rbtn_shutdown;
        private System.Windows.Forms.Button btn_failsafe;
        private System.Windows.Forms.Button btn_start;
        private System.Windows.Forms.RadioButton rbtn_restart;
        private System.Windows.Forms.RadioButton rbtn_lockscreen;
        private System.Windows.Forms.ComboBox cbox_minutes;
        private System.Windows.Forms.ComboBox cbox_hours;
        private System.Windows.Forms.ComboBox cbox_days;
        private System.Windows.Forms.Timer t_timeleft;
        private System.Windows.Forms.Button btn_stop;
    }
}

