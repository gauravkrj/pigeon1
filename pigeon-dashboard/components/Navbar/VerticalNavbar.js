// VerticalNavbar.js
import Link from 'next/link';
import React from 'react';
import Pigeon from '/public/pigeon.gif'
import Image from 'next/image';
import { Lora } from 'next/font/google';
import styles from '../../styles/navbar.module.css'

const lora = Lora({
  weight: "400",
  display: "swap",
  style:"italic",
  subsets:["cyrillic"]
})

const VerticalNavbar = () => {
  return (
    <div
   className={`${styles.vertically} bg-gray-800 h-screen flex flex-col`}
    >
      {/* Vertical Navbar Content */}
      <div className='flex flex-col items-center'>
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
         <Link href="/" className="flex items-center flex-col ">
        <Image src={Pigeon} className=" -scale-x-100 -mr-4 " alt="Pigeon Logo" width={100} height={50} />
            <span className={`${lora.className} text-white ml-2 text-2xl`}>Pigeon</span>
            {/* Use lora instead of Lora */}
        </Link>
        </div>
      </div>

      <nav>
       
        <span className='text-center p-2 flex flex-col text-gray-600'>
        <hr className='border border-slate-700' />
        Your Activity
        <hr className='border border-slate-700' />
        </span>
        <ul className='flex flex-col gap-4 items-left p-2 text-slate-400'>
          {/*          <Link href='/' className='mt-8 '>Take Attendance</Link> */}
          <Link href='/' className='mt-8'>Home</Link>
          <Link href='/create-notification' >Create Notification</Link>
          <Link href='/read-notification'>Read Notification</Link>
          <Link href='/chat' >Chat</Link>
          <Link href='/signup' >Log in</Link>
          <Link href='/about-us' >About Us</Link>
          {/* Add more items if needed */}
        </ul>
      </nav>
    </div>
  );
};

export default VerticalNavbar;
