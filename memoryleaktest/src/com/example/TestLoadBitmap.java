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
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.content.Context;
import java.util.List;
import android.widget.ImageView;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;



public class TestLoadBitmap extends  Activity  
{
	private static final String TAG = "MemoryLeakTest";
	EditText edit_text;
    Button button;
    private ImageView mImageView;
    private final int MAX_NUM = 100;
    private static int pic_index = 0;
    private Bitmap[] pictures = new Bitmap[MAX_NUM];

    private LocationManager mLocationManager = null;

	
	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test_load_bitmap);
		 
		edit_text = (EditText)findViewById(R.id.edit_text);
			
        mImageView = (ImageView) findViewById(R.id.iv_bitmap);
		//Bitmap temp = BitmapFactory.decodeResource(getResources(), R.drawable.b0); 
        //mImageView.setImageBitmap(temp);

		button  =  (Button)findViewById(R.id.button_load_bitmap);
		button.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
            System.gc();
            int index = (pic_index % MAX_NUM);
            int resId = getPictureId(index);
		    pictures[index] = BitmapFactory.decodeResource(getResources(), resId); 
            mImageView.setImageBitmap(pictures[index]);
            Log.d(TAG, "pic_index: " + pic_index + ", ByteCount: " + pictures[index].getByteCount());
            //edit_text.setText();
            pic_index ++;
		}
		});
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

    int getPictureId(int index)
    {
       
       int id = (index % 10);
       if (id == 0)
            return R.drawable.b0;
       else if(id == 1)
            return R.drawable.b1;
       else if(id == 2)
            return R.drawable.b2;
       else if(id == 3)
            return R.drawable.b3;
       else if(id == 4)
            return R.drawable.b4;
       else if(id == 5)
            return R.drawable.b5;
       else if(id == 6)
            return R.drawable.b6;
       else if(id == 7)
            return R.drawable.b7;
       else if(id == 8)
            return R.drawable.b8;
       else if(id == 9)
            return R.drawable.b9;
       else
            return R.drawable.b0;

    }
}
