import React from 'react'
import Head from 'next/head'

import { ChakraProvider, extendTheme } from '@chakra-ui/react'

const colors = {
	brand: {
		900: '#1a365d',
		800: '#153e75',
		700: '#2a69ac',
	},
}
const theme = extendTheme({ colors, })

export const AppWithContext = ({ children }) => {
	return <ChakraProvider theme={theme}>{children}</ChakraProvider>
}

const MyApp = ({ Component, pageProps }: any) => {
	return (
		<>
			<Head>
				<title>Todo App</title>
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
			</Head>
			<AppWithContext>
				<Component {...pageProps} />
			</AppWithContext>
		</>
	)
}

export default MyApp
