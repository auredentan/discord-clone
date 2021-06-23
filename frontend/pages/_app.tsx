import React from 'react'
import Head from 'next/head'

const MyApp = ({ Component, pageProps }: any) => {
	return (
		<>
			<Head>
				<title>Todo App</title>
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
			</Head>

			<Component {...pageProps} />
		</>
	)
}

export default MyApp
