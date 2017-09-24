package com.pyzed.memoryleaktest;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import android.R.string;
import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import java.util.ArrayList;
import android.os.AsyncTask;
import android.os.Handler;
import android.os.Message;
import java.util.TimerTask;
import java.util.Timer;

//ref code: http://blog.nimbledroid.com/2016/05/23/memory-leaks.html
//example for anonymous class leakage

public class TestAnonyClass extends  Activity  
{
	private static final String TAG = "MemoryLeakTest";
	EditText edit_text;
    Button button;
    Button button_handler;
    Button button_thread;
    Button button_timer_task;
    //static ArrayList<Activity> activity = new ArrayList();

	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test_anony_class);
		 
		edit_text = (EditText)findViewById(R.id.edit_text);
		button  =  (Button)findViewById(R.id.button);
		button.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
		    startAsyncTask();
            finish();
		}
		});

		button_handler  =  (Button)findViewById(R.id.button_handler);
		button_handler.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
            createHandler();
            finish();
		}
		});
		
		button_thread  =  (Button)findViewById(R.id.button_thread);
		button_thread.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
            spawnThread();
            finish();
		}
		});

		button_timer_task  =  (Button)findViewById(R.id.button_timer_task);
		button_timer_task.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
            scheduleTimer();
            finish();
		}
		});
	}
/*
 *for AnonymousClass Leakage
*/
    void startAsyncTask() {
        new AsyncTask<Void, Void, Void>() {
                @Override 
                protected Void doInBackground(Void... params) {
                        while(true);
                }
        }.execute();
    }

/*
 *for Handler Leakage
*/
    void createHandler() {
        new Handler() {
                @Override
                public void handleMessage(Message message) {
                    super.handleMessage(message);
                }
        }.postDelayed(new Runnable() {
            @Override
            public void run() {
                while(true);
            }
       }, Long.MAX_VALUE >> 1);
   }
/*
* for Thread leakage
*/
        void spawnThread() {
            new Thread() {
                    @Override
                    public void run() {
                      while(true);
                    }
            }.start();
        }

      /*
      * for Timer Task
      */
      void scheduleTimer() {
          new Timer().schedule(new TimerTask() {
                  @Override
                  public void run() {
                    while(true);
                  }
          }, Long.MAX_VALUE >> 1);
      }

	 @Override
	protected void onResume()
	{  	
	    super.onResume();
	}
	 @Override
	protected void onPause()
	{
		super.onPause();
	}
	 @Override
	protected void onDestroy() 
	{
	    super.onDestroy();
	}
}
